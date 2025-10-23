import pandas as pd
import re
from collections import Counter

# Từ khóa đặc trưng cho laptop
laptop_keywords = [
    'pin', 'trâu', 'cấu hình', 'cpu', 'ram', 'ssd', 'card', 'màn hình',
    'laptop', 'máy tính', 'bàn phím', 'touchpad', 'chuột', 'hiệu năng',
    'xử lý', 'render', 'gaming', 'đồ họa', 'fps', 'battery', 'sạc',
    'windows', 'macbook', 'ổ cứng', 'usb', 'cổng', 'webcam', 'loa',
    'tản nhiệt', 'quạt', 'nóng', 'nặng', 'mỏng', 'nhẹ', 'inch',
    'độ phân giải', 'hoạt động', 'khởi động', 'chạy', 'mượt',
    'lag', 'giật', 'treo', 'reset', 'cài đặt', 'phần mềm'
]

# Từ khóa đặc trưng cho quần áo
clothes_keywords = [
    'vải', 'chất vải', 'form', 'size', 'mặc', 'đẹp', 'xinh', 'tôn dáng',
    'áo', 'quần', 'váy', 'đầm', 'mẫu', 'màu', 'họa tiết', 'kiểu',
    'rộng', 'chật', 'vừa', 'ôm', 'suông', 'dài', 'ngắn', 'tay',
    'cổ', 'túi', 'nút', 'khuy', 'kéo', 'co giãn', 'thoáng mát',
    'mát', 'nóng', 'mùa', 'mặc nhà', 'mặc đi chơi', 'đi làm',
    'giặt', 'phai', 'xù', 'nhăn', 'ủi', 'bền màu', 'cotton',
    'jean', 'kaki', 'lụa', 'len', 'thiết kế', 'sang trọng',
    'phong cách', 'trendy', 'thời trang', 'đơn giản', 'lịch sự',
    'vết xước', 'rách', 'chỉ thừa', 'đường may', 'thêu', 'in'
]

def classify_review(review_text):
    """
    Phân loại review thành 'laptop' hoặc 'clothes' dựa trên từ khóa
    """
    if pd.isna(review_text):
        return 'unknown'
    
    review_lower = review_text.lower()
    
    # Đếm số từ khóa laptop và clothes xuất hiện
    laptop_count = sum(1 for keyword in laptop_keywords if keyword in review_lower)
    clothes_count = sum(1 for keyword in clothes_keywords if keyword in review_lower)
    
    # Quyết định category
    if laptop_count > clothes_count:
        return 'laptop'
    elif clothes_count > laptop_count:
        return 'clothes'
    else:
        # Nếu bằng nhau, random để cân bằng dữ liệu
        # Hoặc có thể dùng item_id để phân chia
        return 'laptop' if hash(review_text) % 2 == 0 else 'clothes'

def main():
    print("Đang đọc file ecom_sontc.csv...")
    df = pd.read_csv('ecom_sontc.csv')
    
    print(f"Tổng số reviews: {len(df)}")
    
    # Tạo cột category
    print("\nĐang phân loại reviews...")
    df['category'] = df['review_text'].apply(classify_review)
    
    # Thống kê
    category_counts = df['category'].value_counts()
    print("\nThống kê phân loại:")
    print(category_counts)
    print(f"\nTỷ lệ:")
    print(category_counts / len(df) * 100)
    
    # Lưu file mới
    output_file = 'ecom_sontc_with_category.csv'
    df.to_csv(output_file, index=False, encoding='utf-8')
    print(f"\nĐã lưu file mới: {output_file}")
    
    # Hiển thị một vài mẫu
    print("\n=== MẪU LAPTOP ===")
    laptop_samples = df[df['category'] == 'laptop'].head(5)
    for idx, row in laptop_samples.iterrows():
        print(f"\nReview: {row['review_text']}")
        print(f"Category: {row['category']}")
    
    print("\n=== MẪU CLOTHES ===")
    clothes_samples = df[df['category'] == 'clothes'].head(5)
    for idx, row in clothes_samples.iterrows():
        print(f"\nReview: {row['review_text']}")
        print(f"Category: {row['category']}")

if __name__ == "__main__":
    main()
