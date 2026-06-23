package tests;

import org.testng.Assert;
import org.testng.annotations.Test;
import org.openqa.selenium.support.ui.ExpectedConditions;
import base.BaseTest;
import pages.DragAndDropPage;

public class InvalidDragTargetTest extends BaseTest {

    @Test
    public void invalidDragTarget() {

        DragAndDropPage page = new DragAndDropPage(driver);

        Assert.assertFalse(driver.getCurrentUrl().contains("dashboard"));

    }

}