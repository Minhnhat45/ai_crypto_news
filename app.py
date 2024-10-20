import streamlit as st
import os
from PIL import Image

st.set_page_config(layout="wide", initial_sidebar_state="expanded")

# Set up session state to track if AI suggestion is open or closed
if 'ai_suggestion_visible' not in st.session_state:
    st.session_state.ai_suggestion_visible = False  # Initially hidden

# Title or Header Section
# st.title("AI Crypto News Analyze")

# Main layout with two columns
# Adjusted the column proportions to give the second column (AI suggestion) more space
col1, col2 = st.columns([4, 1]) # Reduced space for col1, increased for col2s

# col1, col2 = st.columns([2,1])



cont1 = st.container()

# Left Column (Article content)
with col1:
    st.subheader("Bitcoin ETFs surpass $2.1b weekly inflows, whale accumulation mirrors 2020 rally")

    image = Image.open("./articles/article0/thumb0.png")
    st.image(image, use_column_width=True)
    st.write("""
    Spot Bitcoin exchange-traded fund inflows shot up more than 580% this week, as one analyst pointed out that whales were loading up on Bitcoin at a pace akin to the lead-up to the 2020 rally.

    Over the past week, inflows into the 12 spot Bitcoin ETFs reached \$2.13 billion, following six consecutive days of positive inflows. This marks the first time weekly inflows into Bitcoin ETFs have surpassed the \$2 billion mark since March 2024.

    Total net inflows across Bitcoin ETFs have hit a record \$20.94 billion. That’s a milestone that took gold ETFs years to achieve, according to Bloomberg’s Eric Balchunas. Bitcoin products took less than a year.

    Weekly inflows hit their high on Oct. 14, with \$555.86 million flowing into the ETFs, but by Oct. 18, the pace slowed down, dipping to \$273.71 million, according to SoSoValue data.

    None of the funds saw negative flows on the last trading day, with ARK 21Shares’ ARKB leading the pack. The inflows recorded were as follows:
    """)

    st.write("""
    - ARK 21Shares’ ARKB, $109.86 million, 7-day inflow streak.
    - BlackRock’s IBIT, $70.41 million, 5-day inflow streak.
    - Bitwise’s BITB, $35.96 million.
    - VanEck’s HODL, $23.34 million.
    - Fidelity’s FBTC,  $18.0 million, 6-day inflow streak.
    - Invesco’s BTCO, $16.11 million.
    - Franklin Templeton’s EZBC, Wisdom Tree’s BTCW, Grayscale’s GBTC and BTC, and Hashdex’s DEFI saw no flows.
    """)

# Button for API call (Footer Button to show AI suggestion)
def load_article(file_path):
    with open(os.path.join("articles", file_path), "r", encoding="utf-8") as file:
        return file.read()

# Sidebar button to toggle AI suggestions
# if st.sidebar.button("Nhận định của AI"):
#     st.session_state.ai_suggestion_visible = not st.session_state.ai_suggestion_visible



# List of articles and their corresponding file paths
# list_articles = ["article1.txt", "article2.txt", "article3.txt", "article4.txt", "article5.txt"]
# selected_article = st.sidebar.radio("Select an Article to Read", list_articles)
# article_content = load_article(articles[selected_article])
# articles = {
#     "Article 1 Title": "article1.txt",
#     "Article 2 Title": "article2.txt",
#     "Article 3 Title": "article3.txt",
#     "Article 4 Title": "article4.txt",
#     "Article 5 Title": "article5.txt"
# }

# Sidebar with radio buttons to select an article
st.sidebar.title("AI Crypto News Analyze")

# Radio button to select an article


# Load the selected article's content


# Display the selected article's title and content inside the sidebar
# st.sidebar.subheader(selected_article)
# st.sidebar.write(article_content)



with col2:
    st.subheader("AI Analyze:")
    st.write("💲 Coin: $BTC")
    st.write("🟢 Tín hiệu: Tích cực")
    st.write("""
             👉 Nhận định của chuyên gia: 
             - Tiêu cực / tích cực: Bài viết tích cực với sự gia tăng dòng tiền vào ETF Bitcoin và sự tích lũy của "cá voi."\n
             - Xu hướng giá: Xu hướng giá Bitcoin có khả năng tăng trong ngắn hạn và trung hạn.\n
             - Đầu tư hay không: Nên đầu tư nếu có chiến lược dài hạn, quản lý rủi ro cho ngắn hạn.
             """)

    with st.expander("Tóm tắt"):
        st.write("- Các quỹ ETF Bitcoin giao ngay đã chứng kiến dòng tiền hàng tuần vượt 2,13 tỷ đô la, đánh dấu mức tăng 580%, với tổng dòng tiền đạt 20,94 tỷ đô la, thiết lập kỷ lục mới.")
        st.write("- Các \"cá voi\" đang tích lũy Bitcoin, tương tự như các mô hình quan sát được trong đợt tăng giá năm 2020, có thể báo hiệu tâm lý lạc quan.")
        st.write("- Một số quỹ ETF Bitcoin như ARK 21Shares ARKB và BlackRock IBIT đã nhận được dòng tiền đáng kể, trong khi một số quỹ không có dòng tiền.")

# with st.expander("AI Analyze"):
#     st.subheader("Các đồng coin được đề cập:")
#     st.write("- Ethereum (ETH)")

#     st.subheader("Tóm tắt:")
#     st.write("""
#     1. Cá voi Ethereum đã tích lũy 254 triệu USD ETH bất chấp lượng ETH đổ vào sàn giao dịch tăng, cho thấy tâm lý nhà đầu tư lẫn lớn.
#     2. Giá ETH tăng vượt mốc 2.600 USD, nhưng đã có hiện tượng chốt lời, khiến giá giảm từ 2.685 USD xuống còn 2.540 USD, làm bốc hơi 16,6 tỷ USD khỏi vốn hóa thị trường.
#     3. Các quỹ ETF Ethereum đã hoạt động kém, với dòng tiền rút khỏi các quỹ của Mỹ và tổng tài sản khiêm tốn từ quỹ ETF mới ra mắt tại Úc.
#     """)

#     st.subheader("Xu hướng:")
#     st.write("""
#     - Tiêu cực đối với Ethereum: Dù có sự tích lũy từ cá voi, nhưng dòng tiền vào sàn tăng, khả năng chốt lời và hiệu suất kém của các quỹ ETF cho thấy khả năng giá có thể giảm trong ngắn hạn.
#     """)

#     st.subheader("Nhận định của chuyên gia:")
#     st.write("Mặc dù...")
import streamlit as st
from PIL import Image

# Function to create a mini article component
def mini_article(image_path, title, description):
    image = Image.open(image_path)
    st.image(image, use_column_width=True)
    st.write(f"**{title}**")

    st.markdown(description)

# Custom CSS for footer positioning
footer_style = """
    <style>
    .footer {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        background-color: #f1f1f1;
        text-align: center;
        padding: 10px 0;
    }
    </style>
    <div class="footer">
    <p>Footer Content: @MX2024</p>
    </div>
"""
st.markdown(footer_style, unsafe_allow_html=True)

# Create a footer layout with 5 columns
st.write("### Related Article:")

# Set columns for the footer section (5 columns)
col1, col2, col3, col4, col5 = st.columns(5)

# Display 5 mini articles in the footer columns
with col1:
    mini_article("./articles/article1/thumb1.png", 
                 "BlackRock eyes BUIDL token as collateral in crypto derivatives market: report", 
                 "[Click here to read full article](https://crypto.news/blackrock-eyes-buidl-token-as-collateral-in-crypto-derivatives-market-report/)")

with col2:
    mini_article("./articles/article2/thumb2.png", 
                 "Spot Bitcoin ETFs record over $2.1\b inflows in five-day streak, breaking $20\b mark", 
                 "[Click here to read full article](https://crypto.news/spot-bitcoin-etfs-record-over-2-1b-inflows-in-five-day-streak-breaking-20b-mark/)")

with col3:
    mini_article("./articles/article3/thumb3.png", 
                 "Bitcoin heading to 6-figure price, Bitwise CIO says", 

                 "[Click here to read full article](https://crypto.news/bitcoin-heading-to-6-figure-price-bitwise-cio-says/)")

with col4:
    mini_article("./articles/article1/thumb1.png", 
                 "Spot Bitcoin ETFs see four straight days of inflows, surpassing $1.6b, Ether ETFs rebound", 

                 "[Click here to read full article](https://crypto.news/blackrock-eyes-buidl-token-as-collateral-in-crypto-derivatives-market-report/)")

with col5:
    mini_article("./articles/article1/thumb1.png", 
                 "Ethereum whales bought $254m ETH despite rise in exchange inflows", 

                 "[Click here to read full article](https://crypto.news/blackrock-eyes-buidl-token-as-collateral-in-crypto-derivatives-market-report/)")
