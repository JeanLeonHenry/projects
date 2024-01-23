# owiowiParser

Given a recipe URL from the [owiowi cooking blog](https://owiowifouettemoi.com/), parses it into JSON acceptable for the Nextcloud cookbook app.

## Build
Build with `nim c -d:release -d:ssl [source file]`

## Usage
Generates a directory in cwd. So it's a good idea to invoke it in your local Nextcloud recipes folder.


