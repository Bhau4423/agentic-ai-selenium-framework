package pages;

import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.FindBy;
import org.openqa.selenium.support.PageFactory;

public class UploadPage {

    private WebDriver driver;

    @FindBy(id = "file-upload")
    private WebElement file;

    @FindBy(id = "file-submit")
    private WebElement file_submit;

    public UploadPage(WebDriver driver) {
        this.driver = driver;
        PageFactory.initElements(driver, this);
    }

    public WebElement get_file() {
        return file;
    }

    public WebElement get_file_submit() {
        return file_submit;
    }

}