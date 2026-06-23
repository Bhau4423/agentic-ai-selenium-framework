package tests;

import org.testng.Assert;
import org.testng.annotations.Test;
import org.openqa.selenium.support.ui.ExpectedConditions;
import base.BaseTest;
import pages.CheckboxesPage;

public class UncheckCheckboxTest extends BaseTest {

    @Test
    public void uncheckCheckbox() {

        CheckboxesPage page = new CheckboxesPage(driver);

        wait.until(ExpectedConditions.elementToBeClickable(page.get_checkbox_0()));
        page.get_checkbox_0().click();

        Assert.assertTrue(driver.getCurrentUrl().length() > 0);

    }

}