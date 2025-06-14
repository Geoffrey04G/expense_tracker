import streamlit as st

def show_Features():
    st.markdown(
        """
        <h1 style='text-align: center; color: #00ffee; text-shadow: 0 0 15px #00ffee;'>💡 Robo-Saving Features</h1>

        <style>
            .features-grid {
                display: grid;
                grid-template-columns: repeat(2, 1fr);
                gap: 25px;
                padding: 40px;
                justify-items: center;
                max-width: 950px;
                margin: 0 auto;
            }

            @media (max-width: 768px) {
                .features-grid {
                    grid-template-columns: 1fr;
                    padding: 20px;
                }
            }

            .feature-box {
                background-color: #0d0d1a;
                border-radius: 20px;
                padding: 25px;
                width: 100%;
                max-width: 400px;
                color: white;
                box-shadow: 0 0 12px #00ffee;
                transition: transform 0.3s ease, box-shadow 0.3s ease;
                border: 1px solid #00ffee40;
            }

            .feature-box:hover {
                transform: scale(1.05);
                box-shadow: 0 0 25px #00ffee, 0 0 10px #00ffee inset;
            }

            .feature-title {
                font-size: 22px;
                font-weight: bold;
                color: #00ffee;
                margin-bottom: 10px;
                text-shadow: 0 0 5px #00ffee;
            }

            .feature-desc {
                font-size: 15px;
                color: #cccccc;
                line-height: 1.6;
            }
        </style>

        <div class='features-grid'>
            <div class='feature-box'>
                <div class='feature-title'>🧾 Expense Management</div>
                <div class='feature-desc'>Automatically create, approve, and reimburse expenses. Syncs with accounting.</div>
            </div>
            <div class='feature-box'>
                <div class='feature-title'>✈️ Travel</div>
                <div class='feature-desc'>Book flights, hotels, cars — all tracked under expenses for total control.</div>
            </div>
            <div class='feature-box'>
                <div class='feature-title'>💳 Expensify Card</div>
                <div class='feature-desc'>Earn cashbacks and simplify payments through automated billing.</div>
            </div>
            <div class='feature-box'>
                <div class='feature-title'>📸 Receipt Scanning</div>
                <div class='feature-desc'>Snap or upload receipts. We handle the details.</div>
            </div>
            <div class='feature-box'>
                <div class='feature-title'>🔗 Credit Card Import</div>
                <div class='feature-desc'>Auto-import & match corporate card transactions.</div>
            </div>
            <div class='feature-box'>
                <div class='feature-title'>🌍 Global Reimbursements</div>
                <div class='feature-desc'>Pay employees or freelancers in any currency worldwide.</div>
            </div>
            <div class='feature-box'>
                <div class='feature-title'>💻 Virtual Cards</div>
                <div class='feature-desc'>Issue unlimited virtual cards for employees or projects.</div>
            </div>
            <div class='feature-box'>
                <div class='feature-title'>📊 Expense Reports</div>
                <div class='feature-desc'>Submit, review, and approve reports in seconds.</div>
            </div>
            <div class='feature-box'>
                <div class='feature-title'>🤖 AI-Powered Expenses</div>
                <div class='feature-desc'>Categorize, flag policy violations, and reduce errors with AI.</div>
            </div>
             <div class='feature-box'>
                <div class='feature-title'>📱 Mobile App</div>
                <div class='feature-desc'>
                    Manage expenses, cards, and travel on the go. All functionality included.<br><br>
                    <a href='#' style='color:#00ffee; text-decoration:underline;'>Learn More</a>
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )
