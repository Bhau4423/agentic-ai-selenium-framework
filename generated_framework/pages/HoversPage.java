package pages;

import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.FindBy;
import org.openqa.selenium.support.PageFactory;

public class HoversPage {

    private WebDriver driver;

    public HoversPage(WebDriver driver) {
        this.driver = driver;
        PageFactory.initElements(driver, this);
    }

}