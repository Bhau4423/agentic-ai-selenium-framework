package pages;

import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.FindBy;
import org.openqa.selenium.support.PageFactory;

public class ContactPage {

    private WebDriver driver;

    @FindBy(id = "wpforms-161-field_0")
    private WebElement wpforms_fields__0__first_;

    @FindBy(id = "wpforms-161-field_0-last")
    private WebElement wpforms_fields__0__last_;

    @FindBy(id = "wpforms-161-field_1")
    private WebElement wpforms_fields__1_;

    @FindBy(id = "wpforms-161-field-hp")
    private WebElement wpforms_hp_;

    @FindBy(name = "g-recaptcha-hidden")
    private WebElement g_recaptcha_hidden;

    @FindBy(id = "toggle-navigation")
    private WebElement open_menu;

    @FindBy(id = "wpforms-submit-161")
    private WebElement Submit;

    @FindBy(id = "wpforms-161-field_2")
    private WebElement wpforms_fields__2_;

    @FindBy(id = "g-recaptcha-response")
    private WebElement g_recaptcha_response;

    public ContactPage(WebDriver driver) {
        this.driver = driver;
        PageFactory.initElements(driver, this);
    }

    public WebElement get_wpforms_fields__0__first_() {
        return wpforms_fields__0__first_;
    }

    public WebElement get_wpforms_fields__0__last_() {
        return wpforms_fields__0__last_;
    }

    public WebElement get_wpforms_fields__1_() {
        return wpforms_fields__1_;
    }

    public WebElement get_wpforms_hp_() {
        return wpforms_hp_;
    }

    public WebElement get_g_recaptcha_hidden() {
        return g_recaptcha_hidden;
    }

    public WebElement get_open_menu() {
        return open_menu;
    }

    public WebElement get_Submit() {
        return Submit;
    }

    public WebElement get_wpforms_fields__2_() {
        return wpforms_fields__2_;
    }

    public WebElement get_g_recaptcha_response() {
        return g_recaptcha_response;
    }

}