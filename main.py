import os
import ccxt
import numpy as np
import pandas as pd
import mplfinance as mpf
import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from io import BytesIO

# صرافی بایننس
exchange = ccxt.binance()

# ترتیب تایم‌فریم‌ها
timeframes = ['15m', '30m', '1h', '2h', '4h', '1d']
symbols = ['NEIRO/USDT', 'G/USDT', 'CHZ/USDT', 'LTO/USDT', 'ICP/USDT', 'NMR/USDT', 'ONT/USDT', 'RENDER/USDT', 'XTZ/USDT', 'ONE/USDT', 'POLS/USDT', 'GTC/USDT', 'PROM/USDT', 'HFT/USDT', 'T/USDT', 'MOVR/USDT', 'MEME/USDT', 'RLC/USDT', 'MANA/USDT', 'MASK/USDT', 'MINA/USDT', 'SKL/USDT', 'TUSD/USDT', 'FTT/USDT', 'GFT/USDT', 'DASH/USDT', 'DATA/USDT', 'DYDX/USDT', 'DOGE/USDT', 'DOCK/USDT', 'DODO/USDT', 'DOGS/USDT', 'DUSK/USDT', 'DENT/USDT', 'DEGO/USDT', 'HMSTR/USDT', 'AVA/USDT', 'LISTA/USDT', 'POL/USDT', 'OP/USDT', 'CFX/USDT', 'XEC/USDT', 'JASMY/USDT', 'JUP/USDT', 'WRX/USDT', 'SAND/USDT', 'FLOKI/USDT', 'SCRT/USDT', 'SUI/USDT', 'WIF/USDT', 'OMG/USDT', 'GMX/USDT', 'HBAR/USDT', 'AUCTION/USDT', 'NOT/USDT', 'WBTC/USDT', 'LINK/USDT', 'LINA/USDT', 'LQTY/USDT', 'LOKA/USDT', 'HNT/USDT', 'LOOM/USDT', 'LUNA/USDT', 'LUNC/USDT', 'EOS/USDT', 'ACE/USDT', 'GLMR/USDT', 'WIN/USDT', 'WOO/USDT', 'GAS/USDT', 'YFI/USDT', 'AGLD/USDT', 'CHR/USDT', 'ETHDOWN/USDT', 'STORJ/USDT', 'STRAX/USDT', 'INJ/USDT', 'QKC/USDT', 'ERN/USDT', 'PYR/USDT', 'BCH/USDT', 'BAL/USDT', 'ETC/USDT', 'KLAY/USDT', 'QI/USDT', 'DEXE/USDT', 'RPL/USDT', 'KDA/USDT', 'GRT/USDT', 'OMNI/USDT', 'CRV/USDT', 'OSMO/USDT', 'XNO/USDT', 'RDNT/USDT', 'XAI/USDT', 'PHA/USDT', 'LRC/USDT', 'ALT/USDT', 'ACH/USDT', 'CTSI/USDT', 'KSM/USDT', 'VIDT/USDT', 'YGG/USDT', 'CYBER/USDT', 'COMBO/USDT', 'AMB/USDT', 'ZIL/USDT', 'ATA/USDT', 'BAT/USDT', 'TLM/USDT', 'FIDA/USDT', 'BSW/USDT', 'MAGIC/USDT', 'MANTA/USDT', 'METIS/USDT', 'SEI/USDT', 'AR/USDT', 'DYM/USDT', 'GNS/USDT', 'NEO/USDT', 'SLP/USDT', 'TRX/USDT', 'ALPINE/USDT', 'LTC/USDT', 'CVX/USDT', 'TFUEL/USDT', 'THETA/USDT', 'NEAR/USDT', 'LDO/USDT', 'FXS/USDT', 'JTO/USDT', 'TRU/USDT', 'BLUR/USDT', 'EPX/USDT', 'FIL/USDT', 'ATOM/USDT', 'ALGO/USDT', 'ANKR/USDT', 'AVAX/USDT', 'API3/USDT', 'USDC/USDT', 'ARPA/USDT', 'ARKM/USDT', 'SXP/USDT', 'XLM/USDT', 'AXS/USDT', 'EGLD/USDT', 'AUDIO/USDT', 'AERGO/USDT', 'WLD/USDT', 'REN/USDT', 'ILV/USDT', 'GMT/USDT', 'EIGEN/USDT', 'NFP/USDT', 'TRB/USDT', 'ETH/USDT', 'STX/USDT', 'IOTA/USDT', 'IOST/USDT', 'IOTX/USDT', 'MBL/USDT', 'BTCUP/USDT', 'PAXG/USDT', 'PYTH/USDT', 'BLZ/USDT', 'PERP/USDT', 'PEPE/USDT', 'PUNDIX/USDT', 'PEOPLE/USDT', 'PENDLE/USDT', 'TIA/USDT', 'POND/USDT', 'PORTAL/USDT', 'BSV/USDT', 'TNSR/USDT', 'LSK/USDT', 'ELF/USDT', 'TAO/USDT', 'OGN/USDT', 'XMR/USDT', 'SYS/USDT', 'HIFI/USDT', 'ENS/USDT', 'DAR/USDT', 'SOL/USDT', 'JST/USDT', 'DCR/USDT', 'KNC/USDT', 'MAV/USDT', 'REZ/USDT', 'ENJ/USDT', 'IO/USDT', 'UNI/USDT', 'STRK/USDT', 'FORTH/USDT', 'QNT/USDT', 'SHIB/USDT', 'SNX/USDT', 'USDP/USDT', 'USTC/USDT', 'SSV/USDT', 'HARD/USDT', 'BTCDOWN/USDT', 'HIGH/USDT', 'ZRX/USDT', 'WAXP/USDT', 'EDU/USDT', 'ADA/USDT', 'APT/USDT', 'DGB/USDT', 'CKB/USDT', 'IMX/USDT', 'ZK/USDT', 'XRP/USDT', 'SUN/USDT', 'DOT/USDT', 'SYN/USDT', 'SUSHI/USDT', 'SUPER/USDT', 'BTC/USDT', 'OXT/USDT', 'OM/USDT', 'WAVES/USDT', 'ARB/USDT', 'QUICK/USDT', 'TWT/USDT', 'MTL/USDT', 'KAVA/USDT', 'RAY/USDT', 'ORDI/USDT', 'ROSE/USDT', 'RUNE/USDT', 'REEF/USDT', 'STG/USDT', 'BANANA/USDT', 'COTI/USDT', 'COMP/USDT', 'CAKE/USDT', 'ZRO/USDT', 'CATI/USDT', 'BTT/USDT', 'CREAM/USDT', 'TON/USDT', 'CELR/USDT', 'CELO/USDT', 'SFP/USDT', 'ADX/USDT', 'FLOW/USDT', 'BB/USDT', 'FLUX/USDT', 'ICX/USDT', 'W/USDT', 'RVN/USDT', 'LPT/USDT', 'ORN/USDT', 'APE/USDT', 'ENA/USDT', 'RSR/USDT', 'GLM/USDT', 'ID/USDT', 'MKR/USDT', 'XEM/USDT', 'PIXEL/USDT', 'POLYX/USDT', 'LIT/USDT', 'BONK/USDT', 'BOME/USDT', 'AMP/USDT', 'TURBO/USDT', 'NTRN/USDT', 'FET/USDT', 'SLF/USDT', 'UMA/USDT', 'FTM/USDT', 'VANRY/USDT', 'VOXEL/USDT', 'CLV/USDT', 'UNFI/USDT', 'BAND/USDT', 'BICO/USDT', '1INCH/USDT', 'AAVE/USDT', 'AKRO/USDT', 'ASTR/USDT', 'UTK/USDT', 'BOND/USDT', 'C98/USDT', 'REQ/USDT', 'DIA/USDT', 'VET/USDT', 'AEVO/USDT', 'ZEC/USDT', 'BNB/USDT', 'ALPHA/USDT', 'NKN/USDT', 'ALICE/USDT', 'BURGER/USDT', 'ETHFI/USDT', 'ZEN/USDT', 'KMD/USDT']

# اطلاعات ایمیل از متغیرهای محیطی
SENDER_EMAIL = os.getenv("SENDER_EMAIL")
RECEIVER_EMAIL = os.getenv("RECEIVER_EMAIL")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")

def send_email(subject, body, attachments=[]):
    message = MIMEMultipart()
    message["From"] = SENDER_EMAIL
    message["To"] = RECEIVER_EMAIL
    message["Subject"] = subject
    message.attach(MIMEText(body, "plain"))

    for filename, attachment in attachments:
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.getvalue())
        encoders.encode_base64(part)
        part.add_header("Content-Disposition", f"attachment; filename={filename}")
        message.attach(part)

    context = ssl.create_default_context()
    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(SENDER_EMAIL, EMAIL_PASSWORD)
            server.sendmail(SENDER_EMAIL, RECEIVER_EMAIL, message.as_string())
        print("Email sent successfully")
    except Exception as e:
        print(f"Error sending email: {e}")

def get_ohlcv(symbol, timeframe):
    # دریافت داده‌های OHLCV
    ohlcv = exchange.fetch_ohlcv(symbol, timeframe)
    return np.array(ohlcv)

def find_downward_trend(peaks):
    # چک کردن اینکه آیا سه قله به صورت نزولی هستند و یک خط ترند دقیق را تشکیل می‌دهند
    if len(peaks) < 3:
        return False
    return peaks[0][1] > peaks[1][1] > peaks[2][1]

def find_peaks(data):
    peaks = []
    for i in range(1, len(data) - 1):
        high = data[i][2]  # نوک شادوی بالای کندل (high)
        prev_high = data[i-1][2]
        next_high = data[i+1][2]
        
        # چک کردن قله (Peak)
        if high > prev_high and high > next_high:
            peaks.append((i, high))
            
        # نگه داشتن فقط سه قله آخر نزولی
        if len(peaks) > 3:
            peaks.pop(0)
            
    return peaks

def check_trend_break(data, peaks):
    # چک کردن شکست خط ترند و عدم پولبک
    trendline_slope = (peaks[2][1] - peaks[0][1]) / (peaks[2][0] - peaks[0][0])
    trendline_intercept = peaks[0][1] - trendline_slope * peaks[0][0]
    
    # بررسی شکسته شدن خط ترند
    for i in range(peaks[2][0], len(data)):
        high = data[i][2]  # نوک شادوی کندل‌های بعدی
        trend_value = trendline_slope * i + trendline_intercept
        if high > trend_value:
            # شکست اتفاق افتاده
            # حالا باید مطمئن شویم که پولبکی هنوز به خط ترند نزده
            for j in range(i + 1, len(data)):
                low = data[j][3]  # نوک شادوی پایین (low)
                if low <= trend_value:
                    return False  # پولبک زده، موقعیت مناسب نیست
            return True  # پولبک نزده، موقعیت مناسب است
    return False

def plot_chart_with_trendline(symbol, timeframe, data, peaks, candle_count):
    df = pd.DataFrame(data, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
    df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
    df.set_index('timestamp', inplace=True)
    
    # محاسبه و رسم خط روند
    trendline_slope = (peaks[2][1] - peaks[0][1]) / (peaks[2][0] - peaks[0][0])
    trendline_intercept = peaks[0][1] - trendline_slope * peaks[0][0]

    # تولید نمودار
    df_subset = df.tail(candle_count)
    
    # محاسبه x_vals و y_vals برای خط روند
    x_vals = np.arange(peaks[0][0], peaks[2][0] + 1)  # +1 برای اطمینان از اینکه آخرین نقطه در محدوده است
    y_vals = trendline_slope * x_vals + trendline_intercept

    # تنظیمات رسم نمودار
    fig, axlist = mpf.plot(df_subset, type='candle', volume=True, style='yahoo', returnfig=True)

    ax = axlist[0]
    ax.set_yscale('log')  # استفاده از مقیاس لگاریتمی
    # رسم خط روند به صورت خط چین
    ax.plot(df.index[x_vals[x_vals < len(df_subset)]], y_vals[x_vals < len(df_subset)], color='red', linewidth=2, linestyle='--', label='Trendline')
    ax.legend()

    # اضافه کردن عنوان به تصویر
    ax.text(0.05, 0.95, f"{symbol}, {timeframe}, {candle_count} candles", transform=ax.transAxes,
            fontsize=12, verticalalignment='top', horizontalalignment='left', bbox=dict(facecolor='white', alpha=0.5))

    # ذخیره نمودار در حافظه به صورت باینری
    image_stream = BytesIO()
    fig.savefig(image_stream, dpi=100, bbox_inches="tight")
    image_stream.seek(0)
    
    return image_stream

# لیست برای جمع‌آوری پیوست‌های ایمیل
all_attachments = []
email_body = ""

for symbol in symbols:
    for timeframe in timeframes:
        try:
            data = get_ohlcv(symbol, timeframe)
            peaks = find_peaks(data)
            if len(peaks) == 3 and find_downward_trend(peaks):
                if check_trend_break(data, peaks):
                    # رسم نمودار تایم‌فریم اصلی
                    if timeframe in ['15m', '30m']:
                        candle_count = 50
                    elif timeframe == '1h':
                        candle_count = 100
                    elif timeframe in ['2h', '4h']:
                        candle_count = 150
                    elif timeframe == '1d':
                        candle_count = 250

                    chart_image = plot_chart_with_trendline(symbol, timeframe, data, peaks, candle_count)
                    filename = f"{symbol.replace('/', '_')}, {timeframe}, {candle_count} candles.png"
                    all_attachments.append((filename, chart_image))

                    # به‌دست آوردن تایم‌فریم پایین‌تر
                    lower_timeframe_idx = max(0, timeframes.index(timeframe) - 1)
                    lower_tf = timeframes[lower_timeframe_idx]
                    lower_data = get_ohlcv(symbol, lower_tf)
                    lower_peaks = find_peaks(lower_data)

                    # تعیین تعداد کندل‌ها برای تایم‌فریم پایین‌تر
                    if lower_tf in ['15m', '30m']:
                        candle_count = 100
                    elif lower_tf == '1h':
                        candle_count = 150
                    elif lower_tf in ['2h', '4h']:
                        candle_count = 250
                    elif lower_tf == '1d':
                        candle_count = 250

                    # رسم نمودار برای تایم‌فریم پایین‌تر
                    lower_chart_image = plot_chart_with_trendline(symbol, lower_tf, lower_data, lower_peaks, candle_count)
                    lower_filename = f"{symbol.replace('/', '_')}, {lower_tf}, {candle_count} candles.png"
                    all_attachments.append((lower_filename, lower_chart_image))

                    # به‌روزرسانی محتوای ایمیل
                    email_body += f"Found a downward trendline break for {symbol} on {timeframe} timeframe.\n"
                    email_body += f"Main chart: {filename}\n"
                    email_body += f"Lower timeframe chart: {lower_filename}\n"
        
        except Exception as e:
            print(f"Error processing {symbol} on {timeframe}: {e}")

# ارسال ایمیل با تمام پیوست‌ها
if all_attachments:
    email_body += "\nPlease find the attached charts."
    send_email("Downward Trendline Breaks Detected", email_body, all_attachments)
else:
    print("No valid trendline breaks found.")
