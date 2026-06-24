package pages;

import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.FindBy;
import org.openqa.selenium.support.PageFactory;
import org.openqa.selenium.support.ui.Select;

public class ForgotPasswordPage {

    private WebDriver driver;

    @FindBy(id = "file")
    private WebElement file;

    @FindBy(id = "form_submit")
    private WebElement password;

    public ForgotPasswordPage(WebDriver driver) {
        this.driver = driver;
        PageFactory.initElements(driver, this);
    }

    public WebElement get_email() {
        return file;
    }

    public WebElement get_Retrieve_password() {
        return password;
    }

    public void enterEmail(String value) {
        file.clear();
        file.sendKeys(value);
    }

    public boolean isEmailVisible() {
        return file.isDisplayed();
    }

    public void clickRetrievePassword() {
        password.click();
    }

    public boolean isRetrievePasswordVisible() {
        return password.isDisplayed();
    }


    public WebElement get_file() {
        return file;
    }


    public WebElement get_password() {
        return password;
    }

}