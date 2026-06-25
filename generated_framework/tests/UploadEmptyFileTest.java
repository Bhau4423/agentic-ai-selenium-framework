package tests;

import org.testng.Assert;
import org.testng.annotations.Test;
import org.openqa.selenium.support.ui.ExpectedConditions;
import base.BaseTest;
import pages.DownloadPage;

public class UploadEmptyFileTest extends BaseTest {

    @Test
    public void uploadEmptyFile() {

        DownloadPage page = new DownloadPage(driver);

        Assert.assertTrue(driver.getCurrentUrl().contains("dashboard"));

    }

}