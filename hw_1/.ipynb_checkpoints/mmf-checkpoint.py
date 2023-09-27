class SomeModel:
    def predict(self, message: str) -> float:
        return len(message) * 0.5 + 0.3


def predict_message_mood(
    message: str,
    model: SomeModel,
    bad_thresholds: float = 0.3,
    good_thresholds: float = 0.8,
) -> str:
    if model.predict(str) < bad_thresholds:
        return "неуд"
    elif model.predict(str) > good_thresholds:
        return "отл"
    else:
        return "норм"

print(predict_message_mood("Чапаев и пустота", model))
print(predict_message_mood("Вулкан", model))