use serde_json::json;
use serde_json::Value;
use std::fs;

fn main() {
    const ERR: &str = "Error fetching subs.";

    let data = fs::read_to_string("/home/jean-leon/.cache/wtwitch/subscription-cache.json");
    let res: String = match data {
        Ok(content) => content,
        Err(_error) => ERR.to_string(),
    };

    let mut output = String::from("");
    if res != ERR {
        let v: Value = serde_json::from_str(&res).unwrap_or(json!("parsing error"));
        for i in 1..v["data"].as_array().unwrap().len() + 1 {
            let streamer = v["data"][i - 1]["user_name"].as_str().unwrap_or("");
            output.push_str(streamer);
            output.push_str(" ");
        }
        output = output.trim_end().to_string();
    } else {
        output = res;
    }

    if output != "" {
        let state = if output == ERR { "Critical" } else { "Good" };
        let icon = if output == ERR { "bell-slash" } else { "bell" };
        print!(
            "{}",
            json!(
                {
                    "icon" : icon,
                    "text" : format!("{}", output),
            "state" : state,
                })
            .to_string()
        );
    } else {
        print!("{}", json!({"text":"None live.", "icon":"bell-slash"}));
    }
}
