package pages;

import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.FindBy;
import org.openqa.selenium.support.PageFactory;
import org.openqa.selenium.support.ui.Select;

public class JavascriptAlertsPage {

    private WebDriver driver;

    @FindBy(css = "button")
    private WebElement Click_for_JS_Alert;

    @FindBy(css = "button")
    private WebElement Click_for_JS_Confirm;

    @FindBy(css = "button")
    private WebElement Click_for_JS_Prompt;

    public JavascriptAlertsPage(WebDriver driver) {
        this.driver = driver;
        PageFactory.initElements(driver, this);
    }

    public WebElement get_Click_for_JS_Alert() {
        return Click_for_JS_Alert;
    }

    public WebElement get_Click_for_JS_Confirm() {
        return Click_for_JS_Confirm;
    }

    public WebElement get_Click_for_JS_Prompt() {
        return Click_for_JS_Prompt;
    }

    public void clickClickForJsAlert() {
        Click_for_JS_Alert.click();
    }

    public boolean isClickForJsAlertVisible() {
        return Click_for_JS_Alert.isDisplayed();
    }

    public void clickClickForJsConfirm() {
        Click_for_JS_Confirm.click();
    }

    public boolean isClickForJsConfirmVisible() {
        return Click_for_JS_Confirm.isDisplayed();
    }

    public void clickClickForJsPrompt() {
        Click_for_JS_Prompt.click();
    }

    public boolean isClickForJsPromptVisible() {
        return Click_for_JS_Prompt.isDisplayed();
    }

}