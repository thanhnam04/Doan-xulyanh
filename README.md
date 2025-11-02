# Xử Lý Ảnh Trong Miền Tần Số - Nhận Xét Và Kết Luận Các Bộ Lọc

## Giới Thiệu

Báo cáo này trình bày về xử lý ảnh trong miền tần số, tập trung vào các bộ lọc thông thấp (low-pass), thông cao (high-pass) và lọc chặn (notch). Mỗi bộ lọc có ưu và nhược điểm riêng, phù hợp với các ứng dụng khác nhau. Dưới đây là nhận xét chi tiết cho từng loại bộ lọc, bao gồm ưu điểm, nhược điểm và so sánh để xác định bộ lọc nào tốt hơn trong các tình huống cụ thể.

## 1. Bộ Lọc Thông Thấp (Low-Pass Filters)

Bộ lọc thông thấp dùng để làm mờ ảnh, giảm nhiễu và loại bỏ chi tiết nhỏ bằng cách giữ lại tần số thấp và loại bỏ tần số cao.

### 1.1 Bộ Lọc Thông Thấp Lý Tưởng (Ideal Low-Pass Filter - ILPF)

- **Mô tả**: Loại bỏ hoàn toàn tần số cao ngoài bán kính D₀, giữ nguyên tần số thấp bên trong.
- **Ưu điểm**:
  - Đơn giản trong thiết kế và hiểu biết.
  - Loại bỏ hoàn toàn nhiễu tần số cao, hiệu quả cho việc làm mờ mạnh.
- **Nhược điểm**:
  - Gây hiệu ứng chuông (ringing effect) ở biên ảnh, làm xuất hiện vòng tròn giả.
  - Không mượt mà, dẫn đến mất chi tiết biên một cách đột ngột.
- **Đánh giá**: Tốt cho ứng dụng cần làm mờ mạnh nhưng kém trong bảo toàn chi tiết biên.

#### Chi Tiết Đặc Điểm và Tác Dụng

| Nội dung           | Mô tả                                                          |
| ------------------ | -------------------------------------------------------------- |
| Ảnh gốc            | Chứa chi tiết và biên sắc nét, có nhiễu tần số cao             |
| Ảnh sau lọc        | Làm mờ mạnh, loại bỏ nhiễu cao, biên bị mất đột ngột           |
| Độ mịn             | Tăng mạnh sau khi lọc, hình ảnh trở nên mượt mà hơn            |
| Độ sắc nét         | Giảm rõ rệt, các biên vật thể mờ đi                            |
| Phổ tần số ảnh gốc | Năng lượng phân bố đều, có thành phần cao ở rìa                |
| Phổ tần số sau lọc | Trung tâm sáng, rìa tối đi, năng lượng tập trung ở tần số thấp |
| Tác dụng chính     | Giảm nhiễu, làm mờ ảnh, loại bỏ chi tiết nhỏ                   |
| Cơ chế hoạt động   | Loại bỏ thành phần tần số cao ngoài bán kính D₀                |
| Ưu điểm            | Đơn giản, loại bỏ hoàn toàn nhiễu cao                          |
| Ứng dụng           | Làm mờ mạnh, giảm nhiễu trong ảnh quét hoặc vệ tinh            |

### 1.2 Bộ Lọc Thông Thấp Gauss (Gaussian Low-Pass Filter - GLPF)

- **Mô tả**: Sử dụng hàm Gauss để giảm dần tần số cao, với tham số σ kiểm soát độ mờ.
- **Ưu điểm**:
  - Mượt mà, không gây hiệu ứng chuông.
  - Bảo toàn cấu trúc biên tốt hơn, giảm nhiễu tự nhiên.
  - Dễ điều chỉnh qua σ, linh hoạt cho nhiều ứng dụng.
- **Nhược điểm**:
  - Không loại bỏ hoàn toàn tần số cao như Ideal, có thể giữ lại một phần nhiễu.
  - Yêu cầu tính toán nhiều hơn do hàm mũ.
- **Đánh giá**: Tốt nhất trong số các bộ lọc thông thấp, phù hợp cho làm mờ tự nhiên và giảm nhiễu mà không làm méo ảnh.

#### Chi Tiết Đặc Điểm và Tác Dụng

| Nội dung           | Mô tả                                                                     |
| ------------------ | ------------------------------------------------------------------------- |
| Ảnh gốc            | Chứa chi tiết và biên sắc nét, có nhiễu tần số cao                        |
| Ảnh sau lọc        | Làm mờ mượt, giảm nhiễu cao dần, biên được bảo toàn tốt hơn               |
| Độ mịn             | Tăng dần, hình ảnh mượt mà hơn                                            |
| Độ sắc nét         | Giảm nhẹ, biên vẫn tương đối rõ                                           |
| Phổ tần số ảnh gốc | Năng lượng phân bố đều, có thành phần cao ở rìa                           |
| Phổ tần số sau lọc | Trung tâm sáng, rìa mờ dần theo Gauss, năng lượng tập trung ở tần số thấp |
| Tác dụng chính     | Giảm nhiễu tự nhiên, làm mờ ảnh mà không gây hiệu ứng chuông              |
| Cơ chế hoạt động   | Giảm dần tần số cao bằng hàm Gauss                                        |
| Ưu điểm            | Mượt mà, không gây nhiễu biên                                             |
| Ứng dụng           | Làm mờ tự nhiên, giảm nhiễu trong ảnh y tế hoặc thiên văn                 |

### 1.3 Bộ Lọc Thông Thấp Butterworth (Butterworth Low-Pass Filter - BLPF)

- **Mô tả**: Giảm dần tần số cao với cấp n, tần số cắt D₀, mượt hơn Ideal nhưng kém Gauss.
- **Ưu điểm**:
  - Mượt hơn Ideal, giảm hiệu ứng chuông.
  - Linh hoạt với cấp n để điều chỉnh độ dốc.
  - Cân bằng giữa làm mờ và bảo toàn chi tiết.
- **Nhược điểm**:
  - Phức tạp hơn Ideal, yêu cầu chọn n và D₀ phù hợp.
  - Vẫn có thể gây nhiễu nhẹ ở biên nếu n thấp.
- **Đánh giá**: Tốt cho ứng dụng cần kiểm soát độ mờ chính xác, nhưng Gauss thường ưu việt hơn về mượt mà.

### So Sánh Bộ Lọc Thông Thấp

- **Tốt nhất**: Gauss (GLPF) - Mượt, tự nhiên, ít nhiễu biên.
- **Tốt thứ hai**: Butterworth (BLPF) - Linh hoạt, cân bằng.
- **Kém nhất**: Ideal (ILPF) - Gây hiệu ứng chuông, kém thực tế.

## 2. Bộ Lọc Thông Cao (High-Pass Filters)

Bộ lọc thông cao dùng để làm sắc nét ảnh, tăng cường biên và chi tiết bằng cách giữ lại tần số cao và loại bỏ tần số thấp.

### 2.1 Bộ Lọc Thông Cao Lý Tưởng (Ideal High-Pass Filter - IHPF)

- **Mô tả**: Loại bỏ hoàn toàn tần số thấp trong bán kính D₀, giữ nguyên tần số cao bên ngoài.
- **Ưu điểm**:
  - Đơn giản, làm sắc nét mạnh biên ảnh.
  - Hiệu quả cho phát hiện biên rõ ràng.
- **Nhược điểm**:
  - Gây hiệu ứng chuông nghiêm trọng, làm xuất hiện vòng tròn giả quanh biên.
  - Mất chi tiết mượt, ảnh trở nên nhiễu.
- **Đánh giá**: Tốt cho ứng dụng cần biên rõ nhưng kém trong bảo toàn chất lượng ảnh tổng thể.

### 2.2 Bộ Lọc Thông Cao Gauss (Gaussian High-Pass Filter - GHPF)

- **Mô tả**: Sử dụng 1 - hàm Gauss để giảm tần số thấp, với σ kiểm soát độ sắc nét.
- **Ưu điểm**:
  - Mượt mà, không gây hiệu ứng chuông.
  - Tăng cường biên tự nhiên, giảm nhiễu nền.
  - Dễ điều chỉnh, linh hoạt.
- **Nhược điểm**:
  - Không loại bỏ hoàn toàn tần số thấp, có thể giữ lại một phần mờ.
  - Yêu cầu tính toán hàm mũ.
- **Đánh giá**: Tốt nhất cho làm sắc nét tự nhiên, như tăng cường vân tay hoặc chi tiết ảnh.

#### Chi Tiết Đặc Điểm và Tác Dụng

| Nội dung           | Mô tả                                                                |
| ------------------ | -------------------------------------------------------------------- |
| Ảnh gốc            | Chứa nhiều tần số thấp, vùng sáng tối mượt và ít chi tiết            |
| Ảnh sau lọc        | Giữ lại chi tiết và biên, loại bỏ vùng phẳng và chậm biến            |
| Độ mịn             | Giảm mạnh sau khi lọc, hình ảnh trở nên sắc nét hơn                  |
| Độ sắc nét         | Tăng rõ rệt, các biên vật thể nổi bật hơn                            |
| Phổ tần số ảnh gốc | Tập trung năng lượng ở trung tâm (tần số thấp chiếm ưu thế)          |
| Phổ tần số sau lọc | Trung tâm tối đi, năng lượng chuyển ra vùng rìa (tần số cao)         |
| Tác dụng chính     | Nhấn mạnh chi tiết, làm rõ cấu trúc và biên của vật thể              |
| Cơ chế hoạt động   | Loại bỏ thành phần tần số thấp, giữ lại tần số cao trong phổ Fourier |
| Ưu điểm            | Đường cong Gauss trơn, không gây nhiễu hoặc hiện tượng chuông        |
| Ứng dụng           | Tăng cường ảnh, phát hiện biên, làm sắc nét ảnh trong xử lý ảnh số   |

### 2.3 Bộ Lọc Thông Cao Butterworth (Butterworth High-Pass Filter - BHPF)

- **Mô tả**: Giảm tần số thấp với cấp n, tần số cắt D₀, mượt hơn Ideal.
- **Ưu điểm**:
  - Mượt hơn Ideal, giảm hiệu ứng chuông.
  - Linh hoạt với n để điều chỉnh độ sắc nét.
  - Cân bằng giữa tăng cường biên và giảm nhiễu.
- **Nhược điểm**:
  - Phức tạp, cần chọn tham số.
  - Vẫn có thể gây nhiễu nhẹ nếu n không phù hợp.
- **Đánh giá**: Tốt cho ứng dụng cần kiểm soát độ sắc nét, nhưng Gauss thường tốt hơn về mượt mà.

### So Sánh Bộ Lọc Thông Cao

- **Tốt nhất**: Gauss (GHPF) - Mượt, tự nhiên, ít nhiễu.
- **Tốt thứ hai**: Butterworth (BHPF) - Linh hoạt, cân bằng.
- **Kém nhất**: Ideal (IHPF) - Gây hiệu ứng chuông, kém thực tế.

## 3. Bộ Lọc Chặn (Notch Filters)

- **Mô tả**: Loại bỏ tần số cụ thể (như nhiễu chu kỳ) bằng cách đặt vết khuyết tại vị trí tần số nhiễu trong phổ.
- **Ưu điểm**:
  - Chính xác, loại bỏ nhiễu cụ thể mà không ảnh hưởng tần số khác.
  - Hiệu quả cho nhiễu lặp (như đường quét, khảm ảnh).
- **Nhược điểm**:
  - Phức tạp trong xác định vị trí nhiễu.
  - Có thể loại bỏ chi tiết hợp lệ nếu nhiễu chồng lên.
- **Đánh giá**: Tốt cho loại bỏ nhiễu chu kỳ, nhưng yêu cầu phân tích phổ cẩn thận.

## Kết Luận Chung

- **Bộ lọc tốt nhất tổng thể**: Gauss (cả low-pass và high-pass) - Vì mượt mà, ít hiệu ứng phụ, phù hợp đa dạng ứng dụng như giảm nhiễu, tăng cường biên mà không làm méo ảnh.
- **Khi nào dùng Ideal**: Ứng dụng đơn giản, cần hiệu quả nhanh nhưng chấp nhận hiệu ứng chuông.
- **Khi nào dùng Butterworth**: Cần kiểm soát độ lọc qua tham số, như trong kỹ thuật chuyên sâu.
- **Khi nào dùng Notch**: Loại bỏ nhiễu cụ thể, như trong xử lý ảnh quét hoặc vệ tinh.
- **Lời khuyên**: Luôn thử nghiệm với tham số (D₀, σ, n) và so sánh kết quả. Gauss thường là lựa chọn an toàn cho chất lượng ảnh cao.

Báo cáo này dựa trên lý thuyết và ví dụ thực tế, giúp chọn bộ lọc phù hợp cho từng nhiệm vụ xử lý ảnh.

## Tài Liệu Tham Khảo

- Phạm Thế Bảo - Bài giảng Phân tích và xử lý ảnh, Trường Đại học Sài Gòn (2025).
- Rafael C. Gonzalez & Richard E. Woods - Digital Image Processing (Fourth Edition), Pearson (2018).
- Các nguồn khác trong báo cáo LaTeX.
