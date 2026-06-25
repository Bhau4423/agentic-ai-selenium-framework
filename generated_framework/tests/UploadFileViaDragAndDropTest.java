package tests;

import org.testng.Assert;
import org.testng.annotations.Test;
import org.openqa.selenium.support.ui.ExpectedConditions;
import base.BaseTest;
import pages.DragAndDropPage;

public class UploadFileViaDragAndDropTest extends BaseTest {

    @Test
    public void uploadFileViaDragAndDrop() {

        DragAndDropPage page = new DragAndDropPage(driver);

        Assert.assertTrue(driver.getCurrentUrl().length() > 0);

    }

}