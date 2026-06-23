package tests;

import org.testng.Assert;
import org.testng.annotations.Test;
import org.openqa.selenium.support.ui.ExpectedConditions;
import base.BaseTest;
import pages.UploadPage;

public class UploadWithoutFileSelectionTest extends BaseTest {

    @Test
    public void uploadWithoutFileSelection() {

        UploadPage page = new UploadPage(driver);

        wait.until(ExpectedConditions.visibilityOf(page.get_file()));
        // UNKNOWN ACTION : FILE_UPLOAD

        Assert.assertFalse(driver.getCurrentUrl().contains("dashboard"));

    }

}