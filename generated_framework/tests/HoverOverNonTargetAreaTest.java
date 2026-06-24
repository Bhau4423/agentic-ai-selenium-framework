package tests;

import org.testng.Assert;
import org.testng.annotations.Test;
import org.openqa.selenium.support.ui.ExpectedConditions;
import base.BaseTest;
import pages.HoversPage;

public class HoverOverNonTargetAreaTest extends BaseTest {

    @Test
    public void hoverOverNonTargetArea() {

        HoversPage page = new HoversPage(driver);

        Assert.assertFalse(driver.getCurrentUrl().contains("dashboard"));

    }

}