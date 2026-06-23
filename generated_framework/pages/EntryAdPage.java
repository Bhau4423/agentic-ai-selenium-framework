package pages;

import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.FindBy;
import org.openqa.selenium.support.PageFactory;

public class EntryAdPage {

    private WebDriver driver;

    public EntryAdPage(WebDriver driver) {
        this.driver = driver;
        PageFactory.initElements(driver, this);
    }

}