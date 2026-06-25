package tests;

import org.testng.Assert;
import org.testng.annotations.Test;
import org.openqa.selenium.support.ui.ExpectedConditions;
import base.BaseTest;
import pages.HoversPage;

public class HoverOutsideTargetAreaTest extends BaseTest {

    @Test
    public void hoverOutsideTargetArea() {

        HoversPage page = new HoversPage(driver);

        Assert.assertFalse(driver.getCurrentUrl().contains("dashboard"));

    }

}