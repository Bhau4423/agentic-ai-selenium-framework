package tests;

import org.testng.Assert;
import org.testng.annotations.Test;
import org.openqa.selenium.support.ui.ExpectedConditions;
import base.BaseTest;
import pages.ContextMenuPage;

public class LeftClickInContextMenuAreaTest extends BaseTest {

    @Test
    public void leftClickInContextMenuArea() {

        ContextMenuPage page = new ContextMenuPage(driver);

        Assert.assertFalse(driver.getCurrentUrl().contains("dashboard"));

    }

}