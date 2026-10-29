def _validate_scores(scores):
    if not scores:
        raise ValueError("Scores list cannot be empty.")

    validated_scores = []
    for score in scores:
        if score < 0 or score > 100:
            raise ValueError("Each score must be between 0 and 100.")
        validated_scores.append(float(score))

    return validated_scores


def calculate_average(scores):
    validated_scores = _validate_scores(scores)
    return sum(validated_scores) / len(validated_scores)


def get_highest_score(scores):
    validated_scores = _validate_scores(scores)
    return max(validated_scores)


def check_pass_status(scores, passing_threshold=60.0):
    if passing_threshold < 0 or passing_threshold > 100:
        raise ValueError("Passing threshold must be between 0 and 100.")

    return calculate_average(scores) > float(passing_threshold)


def get_grade_letter(score):
    if score < 0 or score > 100:
        raise ValueError("Score must be between 0 and 100.")

    if score >= 90:
        return "A"
    if score >= 80:
        return "B"
    if score >= 70:
        return "C"
    if score >= 60:
        return "D"
    return "F"
