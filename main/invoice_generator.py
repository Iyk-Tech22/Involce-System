"""
    Handles genrating of invoice
"""
import os

def generate(html_file=None, path=None):
    """ Generate invoice base of html template """

    if not html_file or not path:
        raise ValueError("html_file missing or path missing")
        
    try:
        import weasyprint
    except OSError:
        # ADD GTK TO ENV VAR IF GTK IS NOT IN ENV
        GTK_FOLDER = r'C:\Program Files\GTK3-Runtime Win64\bin'
        os.environ['PATH'] = GTK_FOLDER + os.pathsep + os.environ.get('PATH', '')
        print(os.environ["PATH"])
    finally:
        html = weasyprint.HTML(string=html_file)
        html.write_pdf(path)



