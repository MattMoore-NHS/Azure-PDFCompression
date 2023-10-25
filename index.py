from dotenv import load_dotenv
import os

load_dotenv()

License.LicenseKey = os.getenv('LICENSE_KEY')
from ironpdf import *
