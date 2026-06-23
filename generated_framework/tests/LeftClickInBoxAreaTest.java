package tests;

import org.testng.Assert;
import org.testng.annotations.Test;
import org.openqa.selenium.support.ui.ExpectedConditions;
import base.BaseTest;
import pages.ContextMenuPage;

public class LeftClickInBoxAreaTest extends BaseTest {

    @Test
    public void leftClickInBoxArea() {

        ContextMenuPage page = new ContextMenuPage(driver);

        Assert.assertFalse(driver.getCurrentUrl().contains("dashboard"));

    }

}