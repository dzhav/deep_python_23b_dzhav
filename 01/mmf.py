class SomeModel:
    def predict(self, message: str) -> float:
        return len(message) * 0.05 + 0.24


def predict_message_mood(message: str, model: SomeModel,
                         bad_thresholds: float = 0.3,
                         good_thresholds: float = 0.8) -> str:
    if model.predict(message) < bad_thresholds:
        return "неуд"
    elif model.predict(message) > good_thresholds:
        return "отл"
    else:
        return "норм"
