package pages;

import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.FindBy;
import org.openqa.selenium.support.PageFactory;
import org.openqa.selenium.support.ui.Select;

public class CheckboxesPage {

    private WebDriver driver;

    @FindBy(css = "input[type='checkbox']")
    private WebElement checkbox_0;

    @FindBy(css = "input[type='checkbox']")
    private WebElement checkbox_1;

    public CheckboxesPage(WebDriver driver) {
        this.driver = driver;
        PageFactory.initElements(driver, this);
    }

    public WebElement get_checkbox_0() {
        return checkbox_0;
    }

    public WebElement get_checkbox_1() {
        return checkbox_1;
    }

    public void checkCheckbox0() {
        if(!checkbox_0.isSelected()) {
            checkbox_0.click();
        }
    }

    public boolean isCheckbox0Visible() {
        return checkbox_0.isDisplayed();
    }

    public void checkCheckbox1() {
        if(!checkbox_1.isSelected()) {
            checkbox_1.click();
        }
    }

    public boolean isCheckbox1Visible() {
        return checkbox_1.isDisplayed();
    }

}