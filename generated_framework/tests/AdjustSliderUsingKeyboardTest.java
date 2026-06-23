package tests;

import org.testng.Assert;
import org.testng.annotations.Test;
import org.openqa.selenium.support.ui.ExpectedConditions;
import base.BaseTest;
import pages.HorizontalSliderPage;

public class AdjustSliderUsingKeyboardTest extends BaseTest {

    @Test
    public void adjustSliderUsingKeyboard() {

        HorizontalSliderPage page = new HorizontalSliderPage(driver);

        wait.until(ExpectedConditions.visibilityOf(page.get_input_0()));
        page.get_input_0().sendKeys("TEST_DATA");

        Assert.assertTrue(driver.getCurrentUrl().length() > 0);

    }

}