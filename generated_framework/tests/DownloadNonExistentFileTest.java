package tests;

import org.testng.Assert;
import org.testng.annotations.Test;
import org.openqa.selenium.support.ui.ExpectedConditions;
import base.BaseTest;
import pages.DownloadPage;

public class DownloadNonExistentFileTest extends BaseTest {

    @Test
    public void downloadNonExistentFile() {

        DownloadPage page = new DownloadPage(driver);

        Assert.assertFalse(driver.getCurrentUrl().contains("dashboard"));

    }

}