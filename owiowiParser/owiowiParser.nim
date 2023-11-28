import std/htmlparser
import std/xmltree
import std/strtabs
import std/httpclient
import std/strutils
import std/parseopt
import std/[json, jsonutils]
import std/[os, times]

#[
    Implements a Nextcloud-useful subsets of https://schema.org/Recipe
    properties.
]#
type
    Recipe = tuple
        name: string
        description: string
        url: string
        image: string
        prepTime: string
        cookTime: string
        totalTime: string
        recipeCategory: string
        keywords: seq[string]
        recipeYield: int
        tool: seq[string]
        recipeIngredient: seq[string]
        recipeInstructions: seq[string]
        dateCreated: string

proc getElementByClass(html: XmlNode, tag: string, class: string): XmlNode =
    for currentTag in html.findAll(tag):
        if currentTag.attrs.getOrDefault("class") == class:
            result = currentTag
            break

proc fetchRecipeByURL(url: string): XmlNode =
    var client = newHttpClient()
    try:
        var response = client.getContent url
        result = parseHtml response
    finally:
        client.close()

# Init Recipe object
var recipe: Recipe

# Parse args
var p = initOptParser()
while true:
    p.next()
    case p.kind
    of cmdEnd: break
    of cmdArgument:
        when defined(release):
            echo "Will be fetching the url " & p.key
        recipe.url = p.key
        break
    else:
        discard

# Get main HTML
var html: XmlNode
when defined(ssl):
    # online
    html = fetchRecipeByURL(recipe.url)
when not defined(ssl):
    # Using local exemple, ignoring args if any
    html = loadHtml "exemple.html"

# Get title 
var title = html.getElementByClass("h1", "entry-title").innerText.strip
var prefix = title.split(" ")[0]
case prefix.normalize:
    of "le", "la", "les":
        # when not defined(release):
            # echo "Found title $1, starting with prefix $2" % [title, prefix]
        title.removePrefix(prefix)
        title = title.strip
    else:
        discard
recipe.name = title

# Get tags
var tags = html.getElementByClass("div", "tags-links")
for tag in tags.findAll("a"):
    recipe.keywords.add tag.innerText
recipe.keywords.add "owiowi"

# Get entry content
html = html.getElementByClass("div", "entry-content")
var i = 0
for child in html.items:
    let text = child.innerText
    if text.contains("Ingrédients"):
        if text.contains(Digits):
            let index = text.find(Digits)
            recipe.recipeYield = parseInt($(text[index]))
        else:
            recipe.recipeYield = 0
            when defined(release):
                echo "No serving info found. Using 0."
        break
    inc i

# Found ingredients, parse 'em
proc isEmpty(node: XmlNode): bool =
    # NOTE
    # v1, works
    # node.kind == xnText and node.innerText.strip == "" 
    # v2, experimental
    len(node) == 0

for j in i..len(html):
    var el = html[j]
    if (not el.isEmpty) and el.tag == "ul":
        for ingredient in el.items:
            let ingredientText = ingredient.innerText.strip
            if ingredientText != "":
                recipe.recipeIngredient.add(ingredientText)
        i = j + 1
        break

for k in i..len(html):
    var el = html[k]
    # echo el.kind, el.isEmpty, el
    if not el.isEmpty:
        var text = el.innerText
        if text.contains "Partager":
            break
        elif text.strip != "":
            recipe.recipeInstructions.add text.strip

# Recipe is parsed
# Json formatting
var jsonRecipe = recipe.toJson
jsonRecipe["@type"] = %* "Recipe"
jsonRecipe["@context"] = %* "http://schema.org"
jsonRecipe["dateCreated"] = %* $now()

when not defined(release):
    echo $jsonRecipe
when defined(release):
    if not dirExists(recipe.name):
        createDir(recipe.name)
    var path = recipe.name / (recipe.name & ".json")
    echo "Recipe created in " & path
    writeFile(path, $jsonRecipe)

# Submitting post request to API
#[
let client = newHttpClient()
client.headers = newHttpHeaders({
    "accept": "application/json",
    "Content-Type": "application/json",
    "Authorization": "Basic AUTH"
})
var body = $jsonRecipe
echo body
try:
let response = client.post("https://SERVER/apps/cookbook/api/v1/recipes", body = body)
echo response.status
finally:
client.close()
]#
