package pages;

import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.FindBy;
import org.openqa.selenium.support.PageFactory;
import org.openqa.selenium.support.ui.Select;

public class UploadPage {

    private WebDriver driver;

    @FindBy(id = "file-upload")
    private WebElement file;

    @FindBy(id = "file-submit")
    private WebElement file_submit;

    @FindBy(css = "input[type='file']")
    private WebElement input_2;

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

    public WebElement get_input_2() {
        return input_2;
    }

    public void enterFile(String value) {
        file.clear();
        file.sendKeys(value);
    }

    public boolean isFileVisible() {
        return file.isDisplayed();
    }

    public void enterFileSubmit(String value) {
        file_submit.clear();
        file_submit.sendKeys(value);
    }

    public boolean isFileSubmitVisible() {
        return file_submit.isDisplayed();
    }

    public void enterInput2(String value) {
        input_2.clear();
        input_2.sendKeys(value);
    }

    public boolean isInput2Visible() {
        return input_2.isDisplayed();
    }

}