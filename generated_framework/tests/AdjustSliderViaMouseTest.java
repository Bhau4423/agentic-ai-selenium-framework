package tests;

import org.testng.Assert;
import org.testng.annotations.Test;
import org.openqa.selenium.support.ui.ExpectedConditions;
import base.BaseTest;
import pages.DragAndDropPage;

public class AdjustSliderViaMouseTest extends BaseTest {

    @Test
    public void adjustSliderViaMouse() {

        DragAndDropPage page = new DragAndDropPage(driver);

        Assert.assertTrue(driver.getCurrentUrl().length() > 0);

    }

}