from django.shortcuts import render, redirect
from .forms import RegistrationForm
from django.core.mail import send_mail
from django.conf import settings

def landing_page(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            instance = form.save()

            # 📩 Nội dung email chi tiết
            email_subject = '🎓 Xác nhận đăng ký khóa học Gout thành công'
            email_message = f"""
Chào {instance.full_name},

Cảm ơn bạn đã đăng ký tham dự khóa học:

🌿 CHUYÊN VIÊN HỒI PHỤC TẬN GỐC BỆNH GOUT “Người Truyền Thừa”
Chương trình đào tạo đặc biệt của Health Coach Đông Y Việt Nam

⏳ Thời gian học:
- Học 5 ngày liên tục online qua Zoom
- Mỗi buổi 90 phút (học + hỏi đáp)
- Có video ghi hình học lại bất cứ lúc nào
- Kèm 1 buổi tư vấn riêng 1:1 với giảng viên

📌 Học phí: 5.000.000đ/khóa
(Đã bao gồm tài liệu, tư vấn 1:1 và video ghi hình)

🎁 Ưu đãi của bạn:
- Miễn phí bộ tài liệu “Hướng dẫn 30 ngày giảm axit uric tự nhiên”
- Giảm 10% học phí nếu nằm trong 30 người đầu tiên

📩 Chúng tôi sẽ liên hệ sớm để hướng dẫn bước tiếp theo.

Trân trọng,
Ban tổ chức - Health Coach Việt Nam
    
📝 Nội dung khóa học

NGÀY 1: Hiểu đúng về Gout
-Gout là bệnh gì? Vì sao Tây y chữa mãi không hết?
-Đông y nhìn Gout thế nào? Tạng phủ nào bị rối loạn?
NGÀY 2: Phác đồ ăn uống & dưỡng sinh
-Thực phẩm kiêng – nên ăn – tuyệt đối tránh
-Hướng dẫn thực đơn 7 ngày hồi phục
NGÀY 3: Bí mật thất truyền trong Đông Y về Gout
-Phân loại và cơ chế hồi phục Gout hoàn toàn, từ Thầy Đạo.
-14 vấn đề tuyệt đối phải nắm.
-04 câu hỏi “vàng” về sức khỏe nền tảng trên cơ thể Gout. 
NGÀY 4: Thảo dược & sản phẩm hỗ trợ
-Các thảo dược khoa học giúp giảm axit uric tự nhiên
-Phân tích Liệu Trình Kisho và ứng dụng đúng cách
NGÀY 5: Duy trì và phòng ngừa tái phát
-Lập kế hoạch 30 – 90 ngày
-Hướng dẫn đồng hành cùng người thân
-Hỏi đáp chuyên sâu cùng Thầy Đạo
💪 Học xong bạn sẽ đủ tự tin để tự mình chủ động kiểm soát Gout – không còn lo sợ.
            """

            # Gửi email
            send_mail(
                email_subject,
                email_message,
                settings.DEFAULT_FROM_EMAIL,
                [instance.email],
                fail_silently=False
            )

            return redirect('landing:success')
    else:
        form = RegistrationForm()
    return render(request, 'landing/index.html', {'form': form})

def success_page(request):
    return render(request, 'landing/success.html')
