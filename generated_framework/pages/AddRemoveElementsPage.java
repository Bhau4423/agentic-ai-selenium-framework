package pages;

import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.FindBy;
import org.openqa.selenium.support.PageFactory;
import org.openqa.selenium.support.ui.Select;

public class AddRemoveElementsPage {

    private WebDriver driver;

    @FindBy(css = "button")
    private WebElement Add_Element;

    public AddRemoveElementsPage(WebDriver driver) {
        this.driver = driver;
        PageFactory.initElements(driver, this);
    }

    public WebElement get_Add_Element() {
        return Add_Element;
    }

    public void clickAddElement() {
        Add_Element.click();
    }

    public boolean isAddElementVisible() {
        return Add_Element.isDisplayed();
    }

}