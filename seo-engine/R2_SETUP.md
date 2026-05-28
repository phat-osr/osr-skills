# Cloudflare R2 setup — simplified (no custom domain)

**Mục tiêu:** Host **infographic** (ảnh OS Research tự generate bằng nano-banana) trên R2, serve qua `https://pub-xxxxxxx.r2.dev/...` (Cloudflare managed URL, không cần touch DNS provider).

> **Lưu ý workflow (cập nhật 2026-05-28):** Cover + supplementary giờ dùng **link Unsplash trực tiếp** (`images.unsplash.com/...`), KHÔNG re-host. Chỉ infographic mới upload lên R2 (vì là ảnh tự tạo, không có URL upstream ổn định). Bước "migrate hàng loạt ảnh sang R2" đã bị bỏ khỏi pipeline — infographic được upload thẳng lúc generate trong Step 5b của `/osr-seo`.

## Phía cậu cần làm (~5 phút)

### Step 1 — Sign up Cloudflare

1. Vào `https://dash.cloudflare.com/sign-up` → email + password
2. Verify email
3. **Không cần add domain** — chỉ cần account để dùng R2

### Step 2 — Enable R2

1. Login dashboard
2. Sidebar trái → **R2 Object Storage**
3. Click **Purchase R2 Plan** → "Subscribe to R2" (free tier: 10GB storage, 1M reads/month, 0 egress fee — vẫn cần card credit để verify nhưng không bị charge với usage thấp)

### Step 3 — Lấy Account ID

- Cloudflare dashboard → sidebar phải có **Account ID** (32-char hex)
- Copy lại

### Step 4 — Tạo API Token

1. Click avatar góc trên phải → **My Profile**
2. Tab **API Tokens** → **Create Token**
3. Chọn template **"Read and write to Cloudflare R2 Storage"** (hoặc Custom với permission `Account → Cloudflare R2:Edit`)
4. Account Resources: **Include → <your account>**
5. **Continue to summary** → **Create Token**
6. Copy token (chỉ hiện 1 lần)

### Step 5 — Paste vào terminal

Mở terminal và chạy (paste 2 giá trị vào prompt):

```bash
cd /Users/phatnguyen/Downloads/OSR/seo-engine
python3 keyword_research/setup_r2.py
```

Script sẽ hỏi:
- `Cloudflare API Token: ` (paste token from Step 4)
- `Cloudflare Account ID: ` (paste from Step 3)
- `Bucket name [osresearch-cdn]: ` (Enter để dùng default)

Script tự động:
1. Tạo R2 bucket
2. Generate S3-compatible credentials (Access Key ID + Secret)
3. Enable r2.dev public URL
4. Write toàn bộ credentials vào `.env`
5. Test upload + download để verify

Output cuối: `R2_PUBLIC_URL=https://pub-xxxxxxxxxxxxx.r2.dev`

### Step 6 — Xong

Sau khi `.env` có đủ R2 vars, không cần chạy migration thủ công nữa. Mỗi khi `/osr-seo` generate 1 infographic, nó tự upload thẳng lên R2 tại key `articles/{slug}/infographic-{sha1[:8]}.png` (immutable cache). Cover + supplementary giữ nguyên link Unsplash trong body.

## Tóm tắt cost

- R2 free tier vĩnh viễn: 10GB storage, 1M Class A ops, 10M Class B ops mỗi tháng
- Chỉ host infographic (~1-2MB/ảnh, vài ảnh/đợt) → dưới 0.1% của free tier
- Egress qua r2.dev: **miễn phí** (không như S3 charge $0.09/GB)
- Card credit chỉ để verify Cloudflare account, không bị charge nếu xài trong free tier

## Ghi chú

- Infographic point sang `https://pub-xxxxxxxxxxxxx.r2.dev/articles/{slug}/infographic-{hash}.png`
- Cloudflare auto-cache ở 300+ edge data centers
- Có thể upgrade lên custom domain sau (cần thêm CNAME vào DNS provider) — chuyển sang custom domain không phá URL cũ vì R2 supports cả 2
