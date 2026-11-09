from IPython.display import display, HTML

def display_dataframe(df, max_rows=1000):
    n = min(max_rows, len(df))
    table_html = df.head(n).to_html(index=False)

    html = f"""
    <div style="max-height:400px; overflow-y:auto; border:1px solid #ccc;">
        {table_html}
    </div>
    """

    display(HTML(data=html))