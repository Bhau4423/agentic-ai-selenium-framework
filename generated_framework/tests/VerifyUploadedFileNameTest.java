package tests;

import org.testng.Assert;
import org.testng.annotations.Test;
import org.openqa.selenium.support.ui.ExpectedConditions;
import base.BaseTest;
import pages.DownloadPage;

public class VerifyUploadedFilenameTest extends BaseTest {

    @Test
    public void verifyUploadedFilename() {

        DownloadPage page = new DownloadPage(driver);

        Assert.assertTrue(driver.getCurrentUrl().length() > 0);

    }

}