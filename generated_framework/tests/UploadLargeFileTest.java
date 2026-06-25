package tests;

import org.testng.Assert;
import org.testng.annotations.Test;
import org.openqa.selenium.support.ui.ExpectedConditions;
import base.BaseTest;
import pages.DownloadPage;

public class UploadLargeFileTest extends BaseTest {

    @Test
    public void uploadLargeFile() {

        DownloadPage page = new DownloadPage(driver);

        Assert.assertTrue(driver.getCurrentUrl().contains("dashboard"));

    }

}