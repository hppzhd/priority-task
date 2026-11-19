def calculate_priority(tier, urgency, problem_type):
    """Чистая функция расчета приоритета"""
    if problem_type == "SYSTEM_FAILURE":
        return {"priority": "P1", "time": 15, "rule": "Rule 1: System Failure"}
    if tier in ["VIP", "PREMIUM"]:
        return {"priority": "P1", "time": 15, "rule": "Rule 2: VIP/Premium Client"}
    if urgency == "HIGH" and problem_type == "ACCESS":
        return {"priority": "P2", "time": 60, "rule": "Rule 3: High Urgency Access"}
    return {"priority": "P3", "time": 480, "rule": "Rule 4: Default"}

if __name__ == "__main__":
    print("Запуск юнит-тестов...")
    assert calculate_priority("VIP", "LOW", "OTHER")["priority"] == "P1"
    assert calculate_priority("STANDARD", "HIGH", "ACCESS")["priority"] == "P2"
    assert calculate_priority("STANDARD", "LOW", "OTHER")["priority"] == "P3"
    print("✅ Все тесты модуля пройдены!")