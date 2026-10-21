# Bài làm Tuần 11 và Tuần 12

Tác giả: Thanh Dinh

- Tuần 11: Exceptions, tracebacks, debugging, defensive coding
- Tuần 12: Testing với pytest

## Cấu trúc file

```text
weeks/
├── week-11-exceptions/exercises/
│   ├── ex01_try_except.py      # bắt lỗi ValueError
│   ├── ex02_multiple.py        # kiểm tra đầu vào, raise ValueError
│   ├── ex03_custom.py          # tái hiện và sửa bug distance
│   └── ex04_else_finally.py    # try / except / else / finally
└── week-12-testing-pytest/exercises/
    ├── decision.py             # code được test (có sẵn)
    └── test_decision_starter.py  # 4 test pytest
```

## Cách chạy

Chạy từ thư mục gốc của repo (cần Python 3.10 trở lên).

```powershell
python .\weeks\week-11-exceptions\exercises\ex01_try_except.py
python .\weeks\week-11-exceptions\exercises\ex02_multiple.py
python .\weeks\week-11-exceptions\exercises\ex03_custom.py
python .\weeks\week-11-exceptions\exercises\ex04_else_finally.py
```

Cài pytest một lần, rồi chạy test:

```powershell
python -m pip install pytest
python -m pytest .\weeks\week-12-testing-pytest\exercises\test_decision_starter.py -q
```

Kết quả đúng của test: `....` và `[100%]`.

## Tuần 11: nội dung chính

### Bài 1: `try / except ValueError`

```python
raw_turn = "not-a-number"

try:
    turn = int(raw_turn)
except ValueError:
    print("Loi: Khong phai so nguyen")
else:
    print(f"Luot choi hop le: {turn}")
```

- `int("not-a-number")` ném `ValueError` vì chuỗi không phải số.
- Đây là lỗi dự kiến do người dùng nhập sai, nên xử lý bằng `try/except`.
- Chỉ bắt đúng `ValueError`, không dùng `except Exception: pass`. Bắt rộng sẽ che mất các bug thật như `NameError`.
- `else` chỉ chạy khi `try` không có lỗi.

### Bài 2 đến 4

| Bài | Ý chính |
|---|---|
| Bài 2 | Kiểm tra đầu vào ở biên: action ngoài `LOCAL_ACTIONS` thì `raise ValueError`, kèm giá trị sai trong thông báo. |
| Bài 3 | Debug: `distance(1, 4)` từng ra `-3`. Sửa thành `abs(goal - position)` và giữ `assert` làm regression check. |
| Bài 4 | `else` xử lý nhánh thành công, `finally` luôn chạy (ghi log), kể cả khi hàm đã `return`. |

### Quy trình debug

```text
Reproduce -> Read traceback -> Isolate -> Fix -> Re-test
```

Đọc traceback từ dòng cuối (loại lỗi và thông điệp), rồi đi ngược lên dòng code của mình.

## Tuần 12: nội dung chính

Pytest tự tìm file `test_*.py` và hàm `test_*`. Mỗi test dùng `assert` theo cấu trúc Arrange, Act, Assert. Có 4 loại case:

| Test | Loại case | Kiểm tra |
|---|---|---|
| `choose_action(1, 4)` | normal | trả `"right"` |
| `choose_action(4, 4)` | edge | trả `"wait"` khi đã ở đích |
| `validate_turn(0)` | invalid | ném `ValueError` (dùng `pytest.raises`) |
| `choose_action(4, 1)` | regression | trả `"left"`, lỗi cũ luôn trả `"right"` |

Ghi chú:
- Assert đúng action cụ thể thay vì chỉ kiểm tra `in LOCAL_ACTIONS`, vì kiểm tra lỏng thì action sai vẫn pass.
- Test import theo `from exercises.decision import ...` vì thư mục `exercises` có `__init__.py`.
- Khi test fail, không sửa expected value cho xanh. Phải xác nhận contract đúng trước, rồi sửa code hoặc sửa test.

## Liên hệ hai tuần

Tuần 11 làm code ném lỗi đúng chỗ (`validate_turn` ném `ValueError`). Tuần 12 viết test để chứng minh điều đó và giữ cho lỗi cũ không quay lại (`pytest.raises`).
