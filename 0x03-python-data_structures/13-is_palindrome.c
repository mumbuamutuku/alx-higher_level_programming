#include "lists.h"

/**
 * reverse_listint - Reverses a singly-linked listint_t list.
 * @head: A pointer to the starting node of the list to reverse.
 *
 * Return: A pointer to the head of the reversed list.
 */
listint_t *reverse_listint(listint_t **head)
{
	listint_t *node = *head, *next, *prev = NULL;

	while (node)
	{
		next = node->next;
		node->next = prev;
		prev = node;
		node = next;
	}

	*head = prev;
	return (*head);
}
/**
 * is_palindrome - Checks if a singly linked list is a palindrome.
 * @head: A pointer to the head of the linked list.
 *
 * Return: If the linked list is not a palindrome - 0.
 *         If the linked list is a palindrome - 1.
 */
int is_palindrome(listint_t **head)
{
    int i = 0, j;
    size_t count = 0;
    listint_t *front, *rear,, *tmp;

    if (*head == NULL || (*head)->next == NULL)
        return (1);

    tmp = *head;
    while (tmp)
    {
        count++;
        tmp = tmp->next;
    }
    tmp = *head;
    for (j = 0; j < (count / 2) - 1; j++)
    {
        tmp = tmp->next;
    }
    if ((count % 2) == 0 && tmp->n != tmp->next->n)
        return 0;

    tmp = tmp->next->next;
    rear = reverse_listint(&tmp);
    front = rear;

    tmp = *head;
    while (rear)
    {
        if (tmp->n != rear->n)
            return (0);
        tmp = tmp->next;
        rear = rear->next;
    }
    reverse_listint(&front);
    return (1);
}