package pages;

import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.FindBy;
import org.openqa.selenium.support.PageFactory;
import org.openqa.selenium.support.ui.Select;

public class ForgotPasswordPage {

    private WebDriver driver;

    @FindBy(id = "email")
    private WebElement email;

    @FindBy(id = "form_submit")
    private WebElement Retrieve_password;

    public ForgotPasswordPage(WebDriver driver) {
        this.driver = driver;
        PageFactory.initElements(driver, this);
    }

    public WebElement get_email() {
        return email;
    }

    public WebElement get_Retrieve_password() {
        return Retrieve_password;
    }

    public void enterEmail(String value) {
        email.clear();
        email.sendKeys(value);
    }

    public boolean isEmailVisible() {
        return email.isDisplayed();
    }

    public void clickRetrievePassword() {
        Retrieve_password.click();
    }

    public boolean isRetrievePasswordVisible() {
        return Retrieve_password.isDisplayed();
    }

}