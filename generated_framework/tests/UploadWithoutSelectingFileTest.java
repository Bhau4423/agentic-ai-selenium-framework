package tests;

import org.testng.Assert;
import org.testng.annotations.Test;
import org.openqa.selenium.support.ui.ExpectedConditions;
import base.BaseTest;
import pages.DownloadPage;

public class UploadWithoutSelectingFileTest extends BaseTest {

    @Test
    public void uploadWithoutSelectingFile() {

        DownloadPage page = new DownloadPage(driver);

        Assert.assertFalse(driver.getCurrentUrl().contains("dashboard"));

    }

}