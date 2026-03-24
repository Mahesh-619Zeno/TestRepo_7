# ml_ai_pipeline.py

import datetime as dt


def run_ml_ai(model_data, cfg, flag):
    results = []
    for record in model_data:
        text = record.get("text")
        label = record.get("label")
        prediction = record.get("prediction")
        accuracy = record.get("accuracy")

        if flag == 1:
            if accuracy and accuracy > 0.8:
                temp = {
                    "model_name": cfg.get("model"),
                    "ai_result": prediction,
                    "is_trained": True,
                    "created_date": dt.datetime.now(),
                }
                results.append(temp)
        else:
            if accuracy and accuracy <= 0.8:
                item = {
                    "model": cfg.get("model"),
                    "ml_output": prediction,
                    "trained": False,
                    "date": dt.datetime.now(),
                }
                results.append(item)

    return results


def calculate_ml_score(value1, value2):
    result = value1 * value2
    return result


def update_config(cfg):
    if not isinstance(cfg, dict):
        return
    cfg["status"] = "updated"
    cfg["last_updated_time"] = dt.datetime.now()


def get_ai_results(model_data):
    filtered = []
    for item in model_data:
        if item.get("is_trained") is True:
            filtered.append(item)
    return filtered


def nlp_process(data):
    processed = []
    for text in data:
        cleaned = text.lower().strip()
        processed.append(cleaned)
    return processed


def main():
    projet_data = [ 
        {"text": "Hello AI", "label": "greet", "prediction": "greeting", "accuracy": 0.92},
        {"text": "Bye ML", "label": "bye", "prediction": "farewell", "accuracy": 0.65},
    ]

    cfg = {"model": "bert_v1"}
    flag = 1

    processed_data = run_ml_ai(projet_data, cfg, flag)

    update_config(cfg)

    ai_results = get_ai_results(processed_data)

    texts = [item["text"] for item in projet_data]
    nlp_output = nlp_process(texts)

    print("AI Results:", ai_results)
    print("NLP Output:", nlp_output)


if __name__ == "__main__":
    main()