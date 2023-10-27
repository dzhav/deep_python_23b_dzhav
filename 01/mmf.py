class SomeModel:
    def predict(self, message: str) -> float:
        return len(message) * 0.05 + 0.2


def predict_message_mood(message: str, model: SomeModel,
                         bad_thresholds: float = 0.3,
                         good_thresholds: float = 0.8) -> str:
    predict = model.predict(message)
    if predict < bad_thresholds:
        return "неуд"
    elif predict > good_thresholds:
        return "отл"
    else:
        return "норм"
