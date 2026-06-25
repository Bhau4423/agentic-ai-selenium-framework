package pages;

import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.FindBy;
import org.openqa.selenium.support.PageFactory;
import org.openqa.selenium.support.ui.Select;

public class LoginPage {

    private WebDriver driver;

    @FindBy(id = "username")
    private WebElement username;

    @FindBy(id = "password")
    private WebElement password;

    @FindBy(css = "button")
    private WebElement Login;

    public LoginPage(WebDriver driver) {
        this.driver = driver;
        PageFactory.initElements(driver, this);
    }

    public WebElement get_username() {
        return username;
    }

    public WebElement get_password() {
        return password;
    }


    public void enterUsername(String value) {
        username.clear();
        username.sendKeys(value);
    }

    public boolean isUsernameVisible() {
        return username.isDisplayed();
    }

    public void enterPassword(String value) {
        password.clear();
        password.sendKeys(value);
    }

    public boolean isPasswordVisible() {
        return password.isDisplayed();
    }

    public void clickLogin() {
        Login.click();
    }

    public boolean isLoginVisible() {
        return Login.isDisplayed();
    }


    public WebElement get_Login() {
        return Login;
    }

}