package pages;

import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.FindBy;
import org.openqa.selenium.support.PageFactory;

public class TestLoginPage {

    private WebDriver driver;

    @FindBy(id = "username")
    private WebElement username;

    @FindBy(id = "password")
    private WebElement password;

    @FindBy(id = "toggle-navigation")
    private WebElement open_menu;

    @FindBy(id = "submit")
    private WebElement Submit;

    public TestLoginPage(WebDriver driver) {
        this.driver = driver;
        PageFactory.initElements(driver, this);
    }

    public WebElement get_username() {
        return username;
    }

    public WebElement get_password() {
        return password;
    }

    public WebElement get_button_0() {
        return button_0;
    }

    public WebElement get_open_menu() {
        return open_menu;
    }

    public WebElement get_Submit() {
        return Submit;
    }

}