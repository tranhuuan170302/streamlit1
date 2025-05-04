# math_operations.py

def add(a, b):
    """Cộng hai số"""
    return a + b

def subtract(a, b):
    """Trừ hai số"""
    return a - b

def multiply(a, b):
    """Nhân hai số"""
    return a * b

def divide(a, b):
    """Chia hai số, kiểm tra chia cho 0"""
    if b == 0:
        raise ValueError("Không thể chia cho 0")
    return a / b
