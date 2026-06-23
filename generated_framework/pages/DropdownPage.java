package pages;

import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.FindBy;
import org.openqa.selenium.support.PageFactory;

public class DropdownPage {

    private WebDriver driver;

    @FindBy(id = "dropdown")
    private WebElement dropdown;

    public DropdownPage(WebDriver driver) {
        this.driver = driver;
        PageFactory.initElements(driver, this);
    }

    public WebElement get_dropdown() {
        return dropdown;
    }

}