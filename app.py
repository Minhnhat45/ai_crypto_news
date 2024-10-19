import streamlit as st
import os

# Set up session state to track if AI suggestion is open or closed
if 'ai_suggestion_visible' not in st.session_state:
    st.session_state.ai_suggestion_visible = False  # Initially hidden

# Title or Header Section
st.title("AI Crypto News Analyze")

# Main layout with two columns
# Adjusted the column proportions to give the second column (AI suggestion) more space
# col1, col2 = st.columns([4, 3]) # Reduced space for col1, increased for col2s

# col1, col2 = st.columns([2,1])

cont1 = st.container()

# Left Column (Article content)
with cont1:
    st.subheader("Ethereum whales bought $254m ETH despite rise in exchange inflows")

    st.write("""
    Ethereum whales accumulated the asset as it surged above the $2,600 mark despite a notable increase in exchange inflows, triggering mixed signals.
    
    According to data provided by IntoTheBlock, the Ethereum Ethereum eth 0.15% Ethereum large holder inflow almost doubled over the past week—registering a net inflow of 97,220 ETH on Oct. 15 which is worth roughly $254 million at the current price point. 
    
    An increase in an asset’s whale net flow shows accumulation and vice versa, per ITB.
    """)

    st.write("""
    Meanwhile, the Ethereum exchange net flows also shifted from a net outflow of 5,700 ETH on Oct. 13 to a net inflow of 15,000 ETH yesterday. This movement shows that investors are aiming for short-term profits.
    
    On-chain data shows that ETH registered an exchange net inflow of $8.88 million over the past week.
    """)

    st.write("""
    This shift would be considered normal given that the ETH price rose from the 2,400 zone and surpassed $2,600 after two weeks of bearish consolidation.
    """)

# Button for API call (Footer Button to show AI suggestion)
def load_article(file_path):
    with open(os.path.join("articles", file_path), "r", encoding="utf-8") as file:
        return file.read()

# Sidebar button to toggle AI suggestions
# if st.sidebar.button("Nhận định của AI"):
#     st.session_state.ai_suggestion_visible = not st.session_state.ai_suggestion_visible

# List of articles and their corresponding file paths
articles = {
    "Article 1 Title": "article1.txt",
    "Article 2 Title": "article2.txt",
    "Article 3 Title": "article3.txt",
    "Article 4 Title": "article4.txt",
    "Article 5 Title": "article5.txt"
}

# Sidebar with radio buttons to select an article
st.sidebar.title("List Articles related")

# Radio button to select an article
selected_article = st.sidebar.radio("Select an Article to Read", list(articles.keys()))

# Load the selected article's content
article_content = load_article(articles[selected_article])

# Display the selected article's title and content inside the sidebar
st.sidebar.subheader(selected_article)
st.sidebar.write(article_content)

# Display the AI suggestions only if the state is True
# if st.session_state.ai_suggestion_visible:
with st.expander("AI Analyze"):
    st.subheader("Các đồng coin được đề cập:")
    st.write("- Ethereum (ETH)")

    st.subheader("Tóm tắt:")
    st.write("""
    1. Cá voi Ethereum đã tích lũy 254 triệu USD ETH bất chấp lượng ETH đổ vào sàn giao dịch tăng, cho thấy tâm lý nhà đầu tư lẫn lớn.
    2. Giá ETH tăng vượt mốc 2.600 USD, nhưng đã có hiện tượng chốt lời, khiến giá giảm từ 2.685 USD xuống còn 2.540 USD, làm bốc hơi 16,6 tỷ USD khỏi vốn hóa thị trường.
    3. Các quỹ ETF Ethereum đã hoạt động kém, với dòng tiền rút khỏi các quỹ của Mỹ và tổng tài sản khiêm tốn từ quỹ ETF mới ra mắt tại Úc.
    """)

    st.subheader("Xu hướng:")
    st.write("""
    - Tiêu cực đối với Ethereum: Dù có sự tích lũy từ cá voi, nhưng dòng tiền vào sàn tăng, khả năng chốt lời và hiệu suất kém của các quỹ ETF cho thấy khả năng giá có thể giảm trong ngắn hạn.
    """)

    st.subheader("Nhận định của chuyên gia:")
    st.write("Mặc dù...")
