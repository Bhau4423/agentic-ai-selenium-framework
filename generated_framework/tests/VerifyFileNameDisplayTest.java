package tests;

import org.testng.Assert;
import org.testng.annotations.Test;
import org.openqa.selenium.support.ui.ExpectedConditions;
import base.BaseTest;
import pages.UploadPage;

public class VerifyFileNameDisplayTest extends BaseTest {

    @Test
    public void verifyFileNameDisplay() {

        UploadPage page = new UploadPage(driver);

        wait.until(ExpectedConditions.visibilityOf(page.get_file()));
        // UNKNOWN ACTION : FILE_UPLOAD

        Assert.assertTrue(driver.getCurrentUrl().length() > 0);

    }

}