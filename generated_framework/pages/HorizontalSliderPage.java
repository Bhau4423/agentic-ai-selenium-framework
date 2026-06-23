package pages;

import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.FindBy;
import org.openqa.selenium.support.PageFactory;
import org.openqa.selenium.support.ui.Select;

public class HorizontalSliderPage {

    private WebDriver driver;

    @FindBy(css = "input[type='range']")
    private WebElement input_0;

    public HorizontalSliderPage(WebDriver driver) {
        this.driver = driver;
        PageFactory.initElements(driver, this);
    }

    public WebElement get_input_0() {
        return input_0;
    }

    public void enterInput0(String value) {
        input_0.clear();
        input_0.sendKeys(value);
    }

    public boolean isInput0Visible() {
        return input_0.isDisplayed();
    }

}