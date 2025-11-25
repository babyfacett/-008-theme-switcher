import streamlit as st


def apply_theme(mode: str) -> None:
    """Apply a light or dark theme by injecting CSS into the page."""
    if mode == "ライト":
        css = """
        <style>
        [data-testid="stApp"] {
            background-color: white;
            color: black;
        }
        </style>
        """
    else:
        css = """
        <style>
        [data-testid="stApp"] {
            background-color: #0e1117;
            color: #fafafa;
        }
        </style>
        """
    st.markdown(css, unsafe_allow_html=True)


def main():
    """Theme switcher app allowing user to toggle between light and dark modes."""
    st.title("色テーマ変更アプリ")
    st.write("ライトモードとダークモードを切り替えられます。")

    mode = st.radio("テーマを選択してください", ("ライト", "ダーク"))
    apply_theme(mode)

    st.info(f"現在のテーマは {mode} モードです。")


if __name__ == "__main__":
    main()